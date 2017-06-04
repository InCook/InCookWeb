# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20170604_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='participations',
        ),
    ]
