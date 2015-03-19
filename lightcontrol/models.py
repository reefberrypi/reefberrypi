from django.db import models

# Create your models here.

class Mode(models.Model):
    MODES = (
        ('WE', 'Weekend'),
        ('WD', 'Weekday'),
        ('LI', 'Lightning')
    )
    mode = models.CharField(max_length=2, choices=MODES, unique=True)
    def __str__(self):
        return self.get_mode_display()

class LightChannel(models.Model):
    label = models.CharField(max_length=200)
    pin = models.IntegerField()
    max_pulse = models.IntegerField(default=4095)
    max_percentage = models.IntegerField(default = 100)
    use_in_night_mode = models.BooleanField(default=False)
    mode = models.ForeignKey('Mode')
    def __str__(self):              # __unicode__ on Python 2
        return self.label
    class Meta:
        unique_together = ('pin', 'mode')

class Schedule(models.Model):
    time = models.TimeField()
    target = models.IntegerField()
    night_schedule = models.BooleanField(default=False)
    current_percentage = models.IntegerField(editable=False, null=True)
    mode = models.ForeignKey('Mode')
    def __str__(self):              # __unicode__ on Python 2
        return str(self.time)
    class Meta:
        unique_together = ('time', 'mode')