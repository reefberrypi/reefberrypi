import sys
import os
import datetime
import django

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
except SyntaxError:
    pass

def get_schedule_lines():
    if datetime.datetime.now().isoweekday() > 5:
        schedule_lines = Schedule.objects.filter(day__day='WE').select_related('day', 'color_temp').order_by('time')
    else:
        schedule_lines = Schedule.objects.filter(day__day='WD').select_related('day', 'color_temp').order_by('time')
    return schedule_lines

schedule_lines = get_schedule_lines()

for line in schedule_lines:
    if line.time <= datetime.datetime.now().time():
        last_line = line
    if line.time >= datetime.datetime.now().time():
        next_line = line
        break

pin_list = []
for temp in last_line.color_temp.lightconfiguration_set.all():
    pin_list.append(temp.light_channel.pin)
for temp in next_line.color_temp.lightconfiguration_set.all():
    pin_list.append(temp.light_channel.pin)
pin_list = sorted(set(pin_list))

schedule_list = []
for pin in pin_list:
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

print (last_line.time, last_line.target)
print (next_line.time, next_line.target)

today = datetime.date.today()
time_resolution = (datetime.datetime.combine(today, next_line.time) -
                   datetime.datetime.combine(today, last_line.time)).seconds/60
time_diff = (datetime.datetime.now() - datetime.datetime.combine(today, last_line.time)).seconds/60


for i in schedule_list:
    print(i)
    previous_pulse = i['max_start_percentage']/100 * i['previous_target']/100 * i['max_pulse']
    next_pulse = i['max_end_percentage']/100 * i['next_target']/100 * i['max_pulse']
    current_step = ((next_pulse - previous_pulse) / time_resolution) * time_diff
    pulse = previous_pulse + current_step
    print ('Previous pulse: ', previous_pulse)
    print ('Next pulse: ', next_pulse)
    print ('Pulse:', int(pulse))
    print('Current step: ', current_step)
    try:
        pwm.setPWM(i['pin'], 0, pulse)
    except NameError:
        pass