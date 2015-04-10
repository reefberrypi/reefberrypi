import datetime
import time

class LedChannel:
    def __init__(self, label, pin, max_pulse, targets):
        self._label = label
        self._pin = pin
        self._max_pulse = max_pulse
        self._targets = targets

    def _get_target_list(self):
        _index = 0
        for val in self._targets:
            if self._is_time_format(val) is True:
                if datetime.datetime.strptime(val, "%H:%M").time() <= datetime.datetime.now().time():
                    _index = self._targets.index(val)
        if _index+2 >= len(self._targets):
            _target_list = [self._targets[_index], self._targets[_index+1], self._targets[0], self._targets[1]]
        else:
            _target_list = [self._targets[_index], self._targets[_index+1], self._targets[_index+2], self._targets[_index+3]]
        return _target_list

    def pulse(self):
        _t = self._get_target_list()
        _steps_per_minute = (_t[3]-_t[1]) / ((self._make_time(_t[2]) - self._make_time(_t[0])).seconds/60)
        _current_minute = ((datetime.datetime.now() - self._make_time(_t[0])).seconds)/60
        _pulse = int((((_current_minute * _steps_per_minute) + _t[1])/100) * self._max_pulse)

        print(self._label)
        print("Targets: ", _t)
        print("Current minute: ", _current_minute)
        print("Steps per minute: ",_steps_per_minute)
        print("Pulse: ", _pulse)
        return self._pin, 0, _pulse

    def _is_time_format(self, time_string):
        try:
            time.strptime(time_string, '%H:%M')
            return True
        except TypeError:
            return False

    def _make_time(self, time_string):
        return  datetime.datetime.strptime(time_string, "%H:%M")

# class ScheduleCollection:
#     def __init__(self, previous_time, next_time, previous_target, next_target, color_temp):
#         self._previous_time = previous_time
#         self._next_time = next_time
#         self._previous_target = previous_target
#         self._next_target = next_target
#         self._color_temp = color_temp
#
#     def update_pwm(self):
#         pass