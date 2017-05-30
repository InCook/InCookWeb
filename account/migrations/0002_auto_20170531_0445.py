# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20170531_0444'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='account',
            name='key_expires',
        ),
        migrations.AddField(
            model_name='account',
            name='bookmarks',
            field=models.ManyToManyField(related_name='account_bookmarks', to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='account',
            name='likes',
            field=models.ManyToManyField(related_name='account_likes', to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='account',
            name='ratings',
            field=models.ManyToManyField(related_name='account_ratings', to='recipe.Recipe'),
        ),
    ]
