from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(default="Покемон", max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="pokemons")
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)