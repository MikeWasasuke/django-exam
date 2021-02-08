from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# https://stackoverflow.com/questions/15285626/django-self-referential-foreign-key
class PokemonSpecie(models.Model):
    name = models.CharField(max_length=250)
    pokemon_type = models.ManyToManyField('PokemonType', verbose_name='pokemon types')
    evolution_level = models.PositiveIntegerField(blank=True, null=True)
    next_evolution = models.ForeignKey('PokemonSpecie', blank=True, null=True, on_delete=models.CASCADE)

    def show_types(self):
        return ", ".join([p.name for p in self.pokemon_type.all()])

    def __str__(self):
        return self.name


class PokemonType(models.Model):
    name = models.CharField(max_length=150, blank='False')

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    nickname = models.CharField(max_length=150)
    species = models.ForeignKey('PokemonSpecie', on_delete=models.CASCADE)
    level = models.PositiveIntegerField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = 'Pokemon'

    # https://stackoverflow.com/questions/50050862/django-override-model-save/50051005
    def save(self, *args, **kwargs):
        if self.level >= self.species.evolution_level:
            self.species = self.species.next_evolution
        super(Pokemon, self).save(*args, **kwargs)

    def __str__(self):
        return self.nickname

# foreign key https://stackoverflow.com/questions/14663523/foreign-key-django-model
# https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
