# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightcontrol', '0002_auto_20150326_1451'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('color_temp', 'time')]),
        ),
    ]
