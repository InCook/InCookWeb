# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='no_likes',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='score',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cautions',
            field=django_mysql.models.ListCharField(models.CharField(max_length=20), choices=[('Low-Carb', 'Low-Carb'), ('High-Fiber', 'High-Fiber'), ('Low-Fat', 'Low-Fat'), ('High-Protein', 'High-Protein'), ('Low-Sodium', 'Low-Sodium'), ('Balanced', 'Balanced')], max_length=105, null=True, size=5, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='diet_labels',
            field=django_mysql.models.ListCharField(models.CharField(max_length=20), choices=[('Low-Carb', 'Low-Carb'), ('High-Fiber', 'High-Fiber'), ('Low-Fat', 'Low-Fat'), ('High-Protein', 'High-Protein'), ('Low-Sodium', 'Low-Sodium'), ('Balanced', 'Balanced')], max_length=105, null=True, size=5, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='health_labels',
            field=django_mysql.models.ListCharField(models.CharField(max_length=20), choices=[('Tree-Nut-Free', 'Tree-Nut-Free'), ('Paleo', 'Paleo'), ('Vegan', 'Vegan'), ('Gluten-Free', 'Gluten-Free'), ('Peanut-Free', 'Peanut-Free'), ('Vegetarian', 'Vegetarian'), ('Fish-Free', 'Fish-Free'), ('Egg-Free', 'Egg-Free'), ('Shellfish-Free', 'Shellfish-Free'), ('Dairy-Free', 'Dairy-Free'), ('Soy-Free', 'Soy-Free')], max_length=315, null=True, size=15, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
