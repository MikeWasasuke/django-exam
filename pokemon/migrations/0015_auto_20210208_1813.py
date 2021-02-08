# Generated by Django 3.1.6 on 2021-02-08 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0014_auto_20210208_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemonspecie'),
        ),
        migrations.AlterField(
            model_name='pokemonspecie',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemonspecie'),
        ),
    ]
