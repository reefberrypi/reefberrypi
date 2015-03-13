from django.db import models

# Create your models here.

class Mode(models.Model):
    MODES = (
        ('NMWE', 'Night Mode Weekend'),
        ('DMWE', 'Day Mode Weekend'),
        ('NMWD', 'Night Mode Weekday'),
        ('DMWD', 'Day Mode Weekday'),
        ('LIGH', 'Lightning')
    )
    mode = models.CharField(max_length=4, choices=MODES, unique=True)
    def __str__(self):
        return self.get_mode_display()

class LightChannel(models.Model):
    label = models.CharField(max_length=200)
    pin = models.IntegerField()
    max_pulse = models.IntegerField(default=4095)
    max_percentage = models.IntegerField(default = 100)
    mode = models.ForeignKey('Mode')
    def __str__(self):              # __unicode__ on Python 2
        return self.label
    class Meta:
        unique_together = ('pin', 'mode')

class Schedule(models.Model):
    active = models.BooleanField(default=True)
    time = models.TimeField()
    target = models.IntegerField()
    mode = models.ForeignKey('Mode')
    def __str__(self):              # __unicode__ on Python 2
        return str(self.time)
    class Meta:
        unique_together = ('time', 'mode')