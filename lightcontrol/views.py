from django.shortcuts import render

from lightcontrol.models import Mode, Schedule, LightChannel

# Create your views here.
def index(request):
    all_modes_list = Mode.objects.all()
    context = {'all_modes_list': all_modes_list}
    return render(request, 'lightcontrol/index.html', context)
