from django.contrib import admin
from events.models import Event, Group

admin.site.register(Group)
admin.site.register(Event)