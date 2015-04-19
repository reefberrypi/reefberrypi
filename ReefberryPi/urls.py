from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ReefberryPi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('lightcontrol.urls', namespace="index")),
    url(r'^lightcontrol/', include('lightcontrol.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
