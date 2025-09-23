from django.db import models  # noqa F401
from datetime import datetime

# your models here
class Pokemon(models.Model):
    title = models.CharField("Название покемона на русском языке", max_length=50, default="Покемон")
    title_en = models.CharField("Название покемона на английском языке", max_length=50, default="Pokemon")
    title_jp = models.CharField("Название покемона на японском языке", max_length=50, default="ポケモン")
    description = models.CharField("Описание покемона", max_length=1000, blank=False, default="Описание отсутствует")
    evolution = models.ForeignKey("self", verbose_name="Эволюции покемона", blank=True, related_name="evolutions", null=True, on_delete=models.CASCADE)
    image = models.ImageField("Изображение покемона", null=True, blank=True, upload_to="pokemons")
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон, связаный с данной сущностью покемона", on_delete=models.CASCADE, null=True, blank=False)
    lat = models.FloatField("Географическая широта сущности покемона", blank=False, default=0.0)
    lon = models.FloatField("Географическая долгота сущности покемона", blank=False, default=0.0)
    appeared_at = models.DateTimeField("Время появление сущности покемона", blank=False, default=datetime.now())
    disappeared_at = models.DateTimeField("Время исчезновения сущности покемона", blank=False, default=datetime.now())
    level = models.IntegerField("Уровень сущности покемона", blank=False, default=0)
    health = models.IntegerField("Очки здоровья сущности покемона", blank=False, default=0)
    damage = models.IntegerField("Очки урона сущности покемона", blank=False, default=0)
    defense = models.IntegerField("Очки защиты сущности покемона", blank=False, default=0)
    stamina = models.IntegerField("Очки выносливости сущности покемона", blank=False, default=0)