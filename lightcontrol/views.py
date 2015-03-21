from django.shortcuts import render

from lightcontrol.models import ColorTemp, Schedule, LightConfig

# Create your views here.
def index(request):
    all_color_temp_list = ColorTemp.objects.all()
    context = {'all_color_temp_list': all_color_temp_list}
    return render(request, 'lightcontrol/index.html', context)
