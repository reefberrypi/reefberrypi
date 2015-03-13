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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('label', models.CharField(max_length=200)),
                ('pin', models.IntegerField()),
                ('max_pulse', models.IntegerField(default=4095)),
                ('max_percentage', models.IntegerField(default=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('mode', models.CharField(choices=[('NMWE', 'Night Mode Weekend'), ('DMWE', 'Day Mode Weekend'), ('NMWD', 'Night Mode Weekday'), ('DMWD', 'Day Mode Weekday'), ('LIGH', 'Lightning')], max_length=4, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('time', models.TimeField()),
                ('target', models.IntegerField()),
                ('mode', models.ForeignKey(to='lightcontrol.Mode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('time', 'mode')]),
        ),
        migrations.AddField(
            model_name='lightchannel',
            name='mode',
            field=models.ForeignKey(to='lightcontrol.Mode'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='lightchannel',
            unique_together=set([('pin', 'mode')]),
        ),
    ]
