# Generated by Django 3.1.6 on 2021-02-08 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_auto_20210206_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonspecie',
            name='pokemon_type',
        ),
        migrations.AddField(
            model_name='pokemonspecie',
            name='pokemon_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemonspecie'),
        ),
    ]
