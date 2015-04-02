import sys
import os
import datetime
import django

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReefberryPi.settings")
    django.setup()

from lightcontrol.ledcontrol import led
from lightcontrol.models import Schedule, LightConfiguration, ColorTemp, ScheduleDay  # TODO check usage

try:
    from lightcontrol.ledcontrol.Adafruit_PWM_Servo_Driver import PWM
    # Initialise the PWM device using the default address
    pwm = PWM(0x40)
    pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
    # Note if you'd like more debug output you can instead run:
    #pwm = PWM(0x40, debug=True)
except SyntaxError:
    pass

def get_schedule_lines():
    if datetime.datetime.now().isoweekday() > 5:
        schedule_lines = Schedule.objects.filter(day__day='WE').select_related('day', 'color_temp')
    else:
        schedule_lines = Schedule.objects.filter(day__day='WD').select_related('day', 'color_temp')
    return schedule_lines

schedule_lines = get_schedule_lines()
target_id_list = []
for line in schedule_lines:
    if line.time >= datetime.datetime.now().time():
        print (line.time, line.target, line.color_temp)
        for temp in line.color_temp.lightconfiguration_set.all():
            print (temp.light_channel.pin, temp.max_percentage, temp.light_channel.max_pulse)



# now = datetime.datetime.now()
# now_time = now.time()
# if now_time >= datetime.time(10,30) and now_time <= datetime.time(21,30):
#     print ("yes, within the interval")
# else:
#     print ('no')

# for channel in all_channels:
#     channel_id = channel[0]
#     current_schedule = Schedule.objects.filter(lightchannel_id=channel_id).order_by('time')
#     schedule = []
#     for test in current_schedule:
#         time = test.time
#         schedule.append(time.strftime("%H:%M"))  # TODO remove conversion
#         schedule.append(test.target)
#     led_object = led.LedChannel(channel[1],channel[2],channel[3],schedule)
#     led_object.pulse()
#     try:
#         pwm.setPWM(led_object.pulse())
#         print(led_object.pulse())
#     except NameError:
#         pass