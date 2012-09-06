from distribution.models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    list_display = ('name_event','id')

admin.site.register(Event, EventAdmin)