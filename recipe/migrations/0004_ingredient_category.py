# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20170531_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
