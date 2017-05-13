# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170514_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cook',
            old_name='caution',
            new_name='cautions',
        ),
    ]
