# Generated by Django 3.1.6 on 2021-02-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(blank='False', max_length=150, verbose_name='Pokemon'),
        ),
        migrations.AlterField(
            model_name='pokemontype',
            name='pokemon_type',
            field=models.CharField(max_length=150, null=True),
        ),
    ]