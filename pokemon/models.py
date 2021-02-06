from django.db import models


# Create your models here.
class PokemonSpecie(models.Model):
    pokemon_name = models.CharField(max_length=250, blank='False')
    pokemon_type = models.ManyToManyField('PokemonType', blank='False')
    evolution_level = models.IntegerField(null=True)
    next_evolution = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.pokemon_name


class PokemonType(models.Model):
    pokemon_type = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.pokemon_type


# foreign key https://stackoverflow.com/questions/14663523/foreign-key-django-model
class Pokemon(models.Model):
    name = models.CharField(max_length=150, verbose_name="Pokemon", blank='False')
    species = models.ForeignKey('PokemonSpecie', blank='False', on_delete=models.CASCADE)
    level = models.IntegerField(null=True)
    trainer = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
