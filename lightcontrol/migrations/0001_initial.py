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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=200)),
                ('pin', models.IntegerField()),
                ('max_pulse', models.IntegerField(default=4095)),
                ('max_percentage', models.IntegerField(default=100)),
                ('use_in_night_mode', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('mode', models.CharField(unique=True, max_length=2, choices=[('WE', 'Weekend'), ('WD', 'Weekday'), ('LI', 'Lightning')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('time', models.TimeField()),
                ('target', models.IntegerField()),
                ('night_schedule', models.BooleanField(default=False)),
                ('current_percentage', models.IntegerField(editable=False)),
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
