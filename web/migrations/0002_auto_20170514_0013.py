# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='calories',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cook',
            name='category',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='cook',
            name='likeNum',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cook',
            name='name',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='cook',
            name='totalWeight',
            field=models.FloatField(default=0, null=True),
        ),
    ]
