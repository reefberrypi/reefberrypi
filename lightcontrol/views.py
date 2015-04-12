from django.shortcuts import render

from lightcontrol.models import Schedule

# Create your views here.
def index(request):
    all_schedules_list = Schedule.objects.all()
    context = {'all_color_temp_list': all_schedules_list}
    return render(request, 'lightcontrol/index.html', context)
