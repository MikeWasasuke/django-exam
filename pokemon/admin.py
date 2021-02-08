from django.contrib import admin
from .models import PokemonSpecie, PokemonType, Pokemon


# Register your models here.
@admin.register(PokemonSpecie)
class PokemonSpecieAdmin(admin.ModelAdmin):
    list_display = ('pokemon_name',
                    'pokemon_type',
                    'evolution_level',
                    'next_evolution')


admin.site.register(Pokemon)
admin.site.register(PokemonType)
#admin.site.register(PokemonSpecie)

