from django.contrib import admin
from lightcontrol.models import LightChannel, Schedule

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1

class LightChannelAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]

admin.site.register(LightChannel, LightChannelAdmin)
