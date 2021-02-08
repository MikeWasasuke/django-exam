from django.contrib import admin
from .models import PokemonSpecie, PokemonType, Pokemon


# Register your models here.
@admin.register(PokemonSpecie)
class PokemonSpecieAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'evolution_level',
                    'next_evolution',
                    'show_types')

    filter_horizontal=('pokemon_type', )

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nickname',
                    'species',
                    'level',
                    'trainer',
                    )


admin.site.register(PokemonType)
