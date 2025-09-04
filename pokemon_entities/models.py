from django.db import models  # noqa F401
from datetime import datetime

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=50, default="Покемон")
    image = models.ImageField(null=True, blank=True, upload_to="pokemons")
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=False)
    lat = models.FloatField(blank=False, default=0.0)
    lon = models.FloatField(blank=False, default=0.0)
    appeared_at = models.DateTimeField(blank=False, default=datetime.now())
    disappeared_at = models.DateTimeField(blank=False, default=datetime.now())
    level = models.IntegerField(blank=False, default=0)
    health = models.IntegerField(blank=False, default=0)
    damage = models.IntegerField(blank=False, default=0)
    defense = models.IntegerField(blank=False, default=0)
    stamina = models.IntegerField(blank=False, default=0)