# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightcontrol', '0003_auto_20150327_1445'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('color_temp', 'time', 'day')]),
        ),
    ]
