# Generated by Django 3.1.6 on 2021-02-08 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokemon', '0005_auto_20210208_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'verbose_name': 'Pokemon', 'verbose_name_plural': 'Pokemon'},
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(blank='False', max_length=150),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='trainer',
            field=models.ForeignKey(max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
