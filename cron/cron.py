import sys
import os
import django

sys.path.append(os.path.join(os.path.dirname(__file__), '../../ReefberryPi/ReefberryPi'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReefberryPi.settings")
django.setup()

from lightcontrol.ledcontrol import led
from lightcontrol.models import LightChannel, Schedule

try:
    from lightcontrol.ledcontrol.Adafruit_PWM_Servo_Driver import PWM
    # Initialise the PWM device using the default address
    pwm = PWM(0x40)
    pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
    # Note if you'd like more debug output you can instead run:
    #pwm = PWM(0x40, debug=True)
except SyntaxError:
    pass

all_channels = LightChannel.objects.values_list()
for channel in all_channels:
    channel_id = channel[0]
    current_schedule = Schedule.objects.filter(lightchannel_id=channel_id, active=True).order_by('time')
    schedule = []
    for test in current_schedule:
        time = test.time
        schedule.append(time.strftime("%H:%M"))
        schedule.append(test.target)
    led_object = led.LedChannel(channel[1],channel[2],channel[3],schedule)
    led_object.pulse()
    try:
        pwm.setPWM(led_object.pulse())
        print(led_object.pulse())
    except NameError:
        pass

