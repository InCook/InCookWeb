# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_remove_recipe_participations'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='participants',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
