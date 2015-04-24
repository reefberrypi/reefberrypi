from django.db import models


class ColorTemp(models.Model):
    MODES = (
        ('DL', 'Day Light'),
        ('ML', 'Moon Light'),
        ('LI', 'Lightning')
    )
    mode = models.CharField(max_length=2, choices=MODES, unique=True)
    current_percentage = models.IntegerField(default=0, editable=False)  # TODO Delete in case not used

    def __str__(self):              # TODO update to unicode for all models because of Python 2
        return self.get_mode_display()


class LightConfiguration(models.Model):
    mode = models.ForeignKey('ColorTemp')
    light_channel = models.ForeignKey('LightChannel')
    max_percentage = models.IntegerField(default=100)  # TODO force 0><100

    class Meta:
        unique_together = ('mode', 'light_channel')


class LightChannel(models.Model):
    label = models.CharField(max_length=50)
    pin = models.IntegerField(unique=True)
    max_pulse = models.IntegerField(default=4095)
    current_percentage = models.IntegerField(default=0, editable=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.label


class ScheduleDay(models.Model):
    DAYS = (
        ('WE', 'Weekend'),
        ('WD', 'Weekday')
    )
    day = models.CharField(max_length=2, choices=DAYS)

    def __str__(self):
        return self.get_day_display()


class Schedule(models.Model):
    day = models.ForeignKey('ScheduleDay')
    time = models.TimeField()
    target = models.IntegerField()  # TODO force 0><100
    color_temp = models.ForeignKey('ColorTemp')

    def __str__(self):              # __unicode__ on Python 2
        return str(self.time)

    class Meta:
        unique_together = ('color_temp', 'time', 'day')