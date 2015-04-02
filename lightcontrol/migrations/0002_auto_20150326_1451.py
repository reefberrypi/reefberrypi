# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightcontrol', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lightconfiguration',
            unique_together=set([('mode', 'light_channel')]),
        ),
    ]
