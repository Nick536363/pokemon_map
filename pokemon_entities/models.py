from django.db import models  # noqa F401
from datetime import datetime

# your models here
class Pokemon(models.Model):
    title = models.CharField("Русское название", max_length=50, default="Покемон")
    title_en = models.CharField("Английское название", max_length=50, default="Pokemon")
    title_jp = models.CharField("Японское название", max_length=50, default="ポケモン")
    description = models.CharField("Описание", max_length=1000, default="Описание отсутствует")
    previous_evolution = models.ForeignKey("self", verbose_name="Предыдущая эволюция", blank=True, related_name="evolutions", null=True, on_delete=models.PROTECT)
    image = models.ImageField("Изображение", null=True, blank=True, upload_to="pokemons")
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон", on_delete=models.CASCADE, null=True, blank=True)
    lat = models.FloatField("Широта", default=0.0)
    lon = models.FloatField("Долгота", default=0.0)
    appeared_at = models.DateTimeField("Время появление", default=datetime.now())
    disappeared_at = models.DateTimeField("Время исчезновения", default=datetime.now())
    level = models.IntegerField("Уровень", blank=True, default=0)
    health = models.IntegerField("Очки здоровья", blank=True, default=0)
    damage = models.IntegerField("Очки урона", blank=True, default=0)
    defense = models.IntegerField("Очки защиты", blank=True, default=0)
    stamina = models.IntegerField("Очки выносливости", blank=True, default=0)