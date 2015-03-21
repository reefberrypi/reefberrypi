from django.db import models

# Create your models here.

class Mode(models.Model):
    MODES = (
        ('DL', 'Day Light'),
        ('ML', 'Moon Light'),
        ('LI', 'Lightning')
    )
    mode = models.CharField(max_length=2, choices=MODES, unique=True)
    def __str__(self):
        return self.get_mode_display()

class ColorTemp(models.Model):
    mode = models.ForeignKey('Mode')
    max_percentage = models.IntegerField(default = 100)
    light_channel = models.ForeignKey('LightChannel')
    def __str__(self):              # __unicode__ on Python 2
        return self.label

class LightChannel(models.Model):
    label = models.CharField(max_length=50)
    pin = models.IntegerField(unique=True)
    max_pulse = models.IntegerField(default=4095)
    def __str__(self):              # __unicode__ on Python 2
        return self.label

class Days(models.Model):
    DAYS = (
        ('WE', 'Weekend'),
        ('WD', 'Weekday')
    )
    day = models.CharField(max_length=2, choices=DAYS)
    def __str__(self):
        return self.get_day_display()

class Schedule(models.Model):
    time = models.TimeField()
    target = models.IntegerField()
    current_percentage = models.IntegerField(editable=False, null=True)
    color_temp = models.ForeignKey('ColorTemp')
    def __str__(self):              # __unicode__ on Python 2
        return str(self.time)
    class Meta:
        unique_together = ('time', 'ColorTemp')