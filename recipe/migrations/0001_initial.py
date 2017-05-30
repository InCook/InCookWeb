# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_mysql.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=50)),
                ('direction', models.TextField()),
                ('thumbnail', models.CharField(max_length=50, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('calories', models.FloatField(default=0, null=True)),
                ('health_labels', django_mysql.models.ListCharField(models.CharField(max_length=20), size=15, choices=[('Tree-Nut-Free', 'Tree-Nut-Free'), ('Paleo', 'Paleo'), ('Vegan', 'Vegan'), ('Gluten-Free', 'Gluten-Free'), ('Peanut-Free', 'Peanut-Free'), ('Vegetarian', 'Vegetarian'), ('Fish-Free', 'Fish-Free'), ('Egg-Free', 'Egg-Free'), ('Shellfish-Free', 'Shellfish-Free'), ('Dairy-Free', 'Dairy-Free'), ('Soy-Free', 'Soy-Free')], null=True, max_length=315)),
                ('diet_labels', django_mysql.models.ListCharField(models.CharField(max_length=20), size=5, choices=[('Low-Carb', 'Low-Carb'), ('High-Fiber', 'High-Fiber'), ('Low-Fat', 'Low-Fat'), ('High-Protein', 'High-Protein'), ('Low-Sodium', 'Low-Sodium'), ('Balanced', 'Balanced')], null=True, max_length=105)),
                ('cautions', django_mysql.models.ListCharField(models.CharField(max_length=20), size=5, choices=[('Low-Carb', 'Low-Carb'), ('High-Fiber', 'High-Fiber'), ('Low-Fat', 'Low-Fat'), ('High-Protein', 'High-Protein'), ('Low-Sodium', 'Low-Sodium'), ('Balanced', 'Balanced')], null=True, max_length=105)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('ingredients', models.ManyToManyField(to='recipe.Ingredient')),
            ],
        ),
    ]
