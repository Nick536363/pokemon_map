from django.db import models  # noqa F401
from datetime import datetime

# your models here
class Pokemon(models.Model):
    title = models.CharField("Русское название", 
        max_length=50, 
        default="Покемон"
    )
    title_en = models.CharField("Английское название", 
        max_length=50, 
        null=True
    )
    title_jp = models.CharField("Японское название", 
        max_length=50, 
        null=True
    )
    description = models.TextField("Описание")
    previous_evolution = models.ForeignKey("self", 
        verbose_name="Предыдущая эволюция", 
        blank=True, 
        related_name="evolutions", 
        null=True, 
        on_delete=models.PROTECT
    )
    image = models.ImageField("Изображение", 
        null=True, 
        upload_to="pokemons"
    )
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, 
        verbose_name="Покемон", 
        on_delete=models.CASCADE, 
        related_name="pokemons"
    )
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appeared_at = models.DateTimeField(
        "Время появление", 
        default=datetime.now()
    )
    disappeared_at = models.DateTimeField(
        "Время исчезновения", 
        default=datetime.now()
    )
    level = models.IntegerField(
        "Уровень",
        blank=True
    )
    health = models.IntegerField(
        "Очки здоровья", 
        blank=True
    )
    damage = models.IntegerField(
        "Очки урона", 
        blank=True
    )
    defense = models.IntegerField(
        "Очки защиты", 
        blank=True
    )
    stamina = models.IntegerField(
        "Очки выносливости", 
        blank=True
    )