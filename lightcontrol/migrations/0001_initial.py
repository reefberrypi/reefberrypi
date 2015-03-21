# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorTemp',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=2, unique=True, choices=[('DL', 'Day Light'), ('ML', 'Moon Light')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LightConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('max_pulse', models.IntegerField(default=4095)),
                ('max_percentage', models.IntegerField(default=100)),
                ('color_temp', models.ForeignKey(to='lightcontrol.ColorTemp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('target', models.IntegerField()),
                ('current_percentage', models.IntegerField(null=True, editable=False)),
                ('day', models.CharField(max_length=2, choices=[('WE', 'Weekend'), ('WD', 'Weekday')])),
                ('color_temp', models.ForeignKey(to='lightcontrol.LightConfig')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('time', 'day')]),
        ),
        migrations.AlterUniqueTogether(
            name='lightconfig',
            unique_together=set([('pin', 'color_temp')]),
        ),
    ]
