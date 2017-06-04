# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170531_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='likes',
            field=models.ManyToManyField(related_name='account_ikes', to='recipe.Recipe'),
        ),
    ]
