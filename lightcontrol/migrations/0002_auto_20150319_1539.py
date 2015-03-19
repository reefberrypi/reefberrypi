# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightcontrol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='current_percentage',
            field=models.IntegerField(null=True, editable=False),
            preserve_default=True,
        ),
    ]
