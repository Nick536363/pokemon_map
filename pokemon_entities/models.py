from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(default="Покемон", max_length=50)