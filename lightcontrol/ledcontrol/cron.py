import sys
import os
import datetime
import django
import time

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReefberryPi.settings")
    django.setup()

from lightcontrol.models import Schedule

try:
    from lightcontrol.ledcontrol.Adafruit_PWM_Servo_Driver import PWM
    # Initialise the PWM device using the default address
    pwm = PWM(0x40)
    pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
    # Note if you'd like more debug output you can instead run:
    #pwm = PWM(0x40, debug=True)
except SyntaxError as se:
    print se
    pass
except ImportError as ie:
    print ie
    pass

def get_db_schedule_lines():
    if datetime.datetime.now().isoweekday() == 5:
        schedule_lines = Schedule.objects.filter(day__day='WD').select_related('day', 'color_temp').order_by('time')
        next_day_lines = Schedule.objects.filter(day__day='WE').select_related('day', 'color_temp').order_by('time')
    elif datetime.datetime.now().isoweekday() == 6:
        schedule_lines = Schedule.objects.filter(day__day='WE').select_related('day', 'color_temp').order_by('time')
        next_day_lines = schedule_lines
    elif datetime.datetime.now().isoweekday() == 7:
        schedule_lines = Schedule.objects.filter(day__day='WE').select_related('day', 'color_temp').order_by('time')
        next_day_lines = Schedule.objects.filter(day__day='WD').select_related('day', 'color_temp').order_by('time')
    else:
        schedule_lines = Schedule.objects.filter(day__day='WD').select_related('day', 'color_temp').order_by('time')
        next_day_lines = schedule_lines
    return schedule_lines, next_day_lines

def create_schedule():
    schedule_lines, next_day_lines = get_db_schedule_lines()
    for line in next_day_lines:
        if line.time <= datetime.datetime.now().time():
            next_day_line = line
            break
    for line in schedule_lines:
        if line.time <= datetime.datetime.now().time():
            last_line = line
    next_line = next_day_line
    for line in reversed(schedule_lines):
        if line.time >= datetime.datetime.now().time():
            next_line = line
    return last_line, next_line

# first_line, last_line, next_line = get_schedule_lines()

def get_pin_list():
    pin_list = []
    for temp in last_line.color_temp.lightconfiguration_set.all():
        pin_list.append(temp.light_channel.pin)
    for temp in next_line.color_temp.lightconfiguration_set.all():
        pin_list.append(temp.light_channel.pin)
    pin_list = sorted(set(pin_list))
    return pin_list

def format_schedule_list():
    schedule_list = []
    for pin in get_pin_list():
        schedule_list.append({'pin':pin, 'previous_target': 0, 'next_target': 0
            , 'previous_time': '', 'next_time': '', 'max_start_percentage': 0
            , 'max_end_percentage': 0, 'max_pulse': 0})

    for temp in last_line.color_temp.lightconfiguration_set.all():
        for item in schedule_list:
            if item['pin'] == temp.light_channel.pin:
                item['previous_target'] = last_line.target
                item['previous_time'] = last_line.time
                item['previous_target'] = last_line.target
                item['max_start_percentage'] = temp.max_percentage
                item['max_pulse'] = temp.light_channel.max_pulse

    for temp in next_line.color_temp.lightconfiguration_set.all():
        for item in schedule_list:
            if item['pin'] == temp.light_channel.pin:
                item['next_target'] = next_line.target
                item['next_time'] = next_line.time
                item['max_end_percentage'] = temp.max_percentage
    return schedule_list

def set_lights():
    time_resolution = (datetime.datetime.combine(datetime.date.today(), next_line.time) -
                       datetime.datetime.combine(datetime.date.today(), last_line.time)).seconds/60
    time_diff = (datetime.datetime.now() - datetime.datetime.combine(datetime.date.today(), last_line.time)).seconds/60
    for i in format_schedule_list():
        previous_pulse = float(i['max_start_percentage'])/100 * float(i['previous_target'])/100 * i['max_pulse']
        next_pulse = float(i['max_end_percentage'])/100 * float(i['next_target'])/100 * i['max_pulse']
        current_step = ((next_pulse - previous_pulse) / time_resolution) * time_diff
        pulse = previous_pulse + current_step
        pulse = int(pulse)
        print "pulse: ", pulse
        print ('Values: ', i['pin'], 0, pulse)
        try:
            pwm.setPWM(i['pin'], 0, pulse)
        except NameError as ne:
            print ne
            pass

while True:
    last_line, next_line = create_schedule()
    print (last_line)
    print (next_line)

    set_lights()
    time.sleep(60)