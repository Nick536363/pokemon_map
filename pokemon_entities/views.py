import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import localtime
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def get_img_url(request, image):
    return request.build_absolute_uri(image.url) if image else DEFAULT_IMAGE_URL


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon, appeared_at__lte=localtime(), disappeared_at__gte=localtime()):
            add_pokemon(
                folium_map, pokemon_entity.lat,
                pokemon_entity.lon,
                get_img_url(request, pokemon.image)
            )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url':  get_img_url(request, pokemon.image),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()

    requested_pokemon = get_object_or_404(pokemons, pk=pokemon_id)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=requested_pokemon, appeared_at__lte=localtime(), disappeared_at__gte=localtime()):
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            get_img_url(request, requested_pokemon.image)
        )
    previous_evolution = None
    next_evolution = None
    if requested_pokemon.previous_evolution:
        previous_evolution = {
            "title_ru": requested_pokemon.previous_evolution.title,
            "img_url": get_img_url(request, requested_pokemon.previous_evolution.image),
            "pokemon_id": requested_pokemon.previous_evolution.id
        }
    if requested_pokemon.next_evolutions.first():
        next_evolution = {
            "title_ru": requested_pokemon.next_evolutions.first().title,
            "img_url": get_img_url(request, requested_pokemon.next_evolutions.first().image),
            "pokemon_id": requested_pokemon.next_evolutions.first().id
        }
    pokemon = {
        "pokemon_id": requested_pokemon.id,
        "description": requested_pokemon.description,
        "title_ru": requested_pokemon.title,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "previous_evolution": previous_evolution,
        "next_evolution": next_evolution,
        "img_url": get_img_url(request, requested_pokemon.image)
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
