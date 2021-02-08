from django.db import models


# Create your models here.
# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/self_fk.html
class PokemonSpecie(models.Model):
    pokemon_name = models.CharField(max_length=250, blank='False')
    pokemon_type = models.ForeignKey('PokemonType', on_delete=models.CASCADE, null=True)
    evolution_level = models.PositiveIntegerField(null=True)
    next_evolution = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.pokemon_name


class PokemonType(models.Model):
    pokemon_type = models.CharField(max_length=150, blank='False')

    def __str__(self):
        return self.pokemon_type


class Pokemon(models.Model):
    name = models.CharField(max_length=150, verbose_name="Pokemon", blank='False')
    species = models.ForeignKey('PokemonSpecie', blank='False', on_delete=models.CASCADE)
    level = models.PositiveIntegerField(null=True)
    trainer = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

# foreign key https://stackoverflow.com/questions/14663523/foreign-key-django-model
# https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
