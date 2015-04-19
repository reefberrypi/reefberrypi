from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import LightChannel


class IndexView(generic.ListView):
    template_name = 'lightcontrol/index.html'
    context_object_name = 'all_lightchannels_list'

    def get_queryset(self):
        return LightChannel.objects.all()

class DetailView(generic.DetailView):
    model = LightChannel
    template_name = 'lightcontrol/detail.html'