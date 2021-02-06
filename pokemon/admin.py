from django.contrib import admin
from .models import PokemonSpecie, PokemonType, Pokemon
# Register your models here.
admin.site.register(Pokemon)
admin.site.register(PokemonType)
admin.site.register(PokemonSpecie)