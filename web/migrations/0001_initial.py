# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('recipe_url', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
                ('totalWeight', models.FloatField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.TextField(null=True)),
                ('totalDaily', models.TextField(null=True)),
                ('dietLabels', models.TextField(null=True)),
                ('calories', models.FloatField(null=True)),
                ('healthLabels', models.TextField(null=True)),
                ('digest', models.TextField(null=True)),
                ('caution', models.TextField(null=True)),
                ('likeNum', models.IntegerField(null=True, blank=True)),
                ('tools', models.TextField(null=True)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
