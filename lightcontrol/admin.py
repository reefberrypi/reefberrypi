from django.contrib import admin
from lightcontrol.models import LightChannel, ScheduleDay, Schedule, ColorTemp, LightConfiguration

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1

class ScheduleDayAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]

class LightConfigurationInline(admin.TabularInline):
    model = LightConfiguration
    extra = 1

class ColorTempAdmin(admin.ModelAdmin):
    inlines = [LightConfigurationInline]

admin.site.register(LightChannel)
admin.site.register(ScheduleDay, ScheduleDayAdmin)
admin.site.register(ColorTemp, ColorTempAdmin)

