# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LightChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('pin', models.IntegerField()),
                ('max_pulse', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('time', models.TimeField()),
                ('target', models.IntegerField()),
                ('lightchannel', models.ForeignKey(to='lightcontrol.LightChannel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
