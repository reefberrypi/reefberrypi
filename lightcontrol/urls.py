__author__ = 'outm'

from django.conf.urls import patterns, url
from lightcontrol import views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
