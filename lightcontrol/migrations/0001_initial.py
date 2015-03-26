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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('mode', models.CharField(choices=[('DL', 'Day Light'), ('ML', 'Moon Light'), ('LI', 'Lightning')], unique=True, max_length=2)),
                ('current_percentage', models.IntegerField(editable=False, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LightChannel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('pin', models.IntegerField(unique=True)),
                ('max_pulse', models.IntegerField(default=4095)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LightConfiguration',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('max_percentage', models.IntegerField(default=100)),
                ('light_channel', models.ForeignKey(to='lightcontrol.LightChannel')),
                ('mode', models.ForeignKey(to='lightcontrol.ColorTemp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('time', models.TimeField()),
                ('target', models.IntegerField()),
                ('color_temp', models.ForeignKey(to='lightcontrol.ColorTemp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScheduleDay',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('day', models.CharField(choices=[('WE', 'Weekend'), ('WD', 'Weekday')], max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.ForeignKey(to='lightcontrol.ScheduleDay'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('day', 'time')]),
        ),
    ]
