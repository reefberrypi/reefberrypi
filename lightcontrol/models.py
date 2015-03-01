from django.db import models

# Create your models here.

class LightChannel(models.Model):
    label = models.CharField(max_length=200)
    pin = models.IntegerField()
    max_pulse = models.IntegerField()
    def __str__(self):              # __unicode__ on Python 2
        return self.label

class Schedule(models.Model):
    lightchannel = models.ForeignKey(LightChannel)
    label = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    time = models.TimeField()
    target = models.IntegerField()