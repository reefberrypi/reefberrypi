# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightcontrol', '0004_auto_20150327_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightchannel',
            name='current_percentage',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
    ]
