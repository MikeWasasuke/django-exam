# Generated by Django 3.1.6 on 2021-02-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20210206_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pokemonspecie',
            name='evolution_level',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pokemonspecie',
            name='next_evolution',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pokemontype',
            name='pokemon_type',
            field=models.CharField(blank='False', max_length=150),
        ),
    ]