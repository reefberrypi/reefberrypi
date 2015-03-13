from django.contrib import admin
from lightcontrol.models import Mode, LightChannel, Schedule

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1

class LightChannelInline(admin.TabularInline):
    model = LightChannel
    extra = 1

class ModeAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline, LightChannelInline]

admin.site.register(Mode, ModeAdmin)
