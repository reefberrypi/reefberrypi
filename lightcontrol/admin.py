from django.contrib import admin
from lightcontrol.models import ColorTemp, LightConfig, Schedule

class LightConfigInline(admin.TabularInline):
    model = LightConfig
    extra = 1

class ColorTempAdmin(admin.ModelAdmin):
    inlines = [LightConfigInline]

admin.site.register(ColorTemp, ColorTempAdmin)
admin.site.register(Schedule)
