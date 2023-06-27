from django.contrib import admin

from .models import Room, Message, Topic


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'host']

    class Meta:
        ordering = ['-created']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['body', 'user']


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Topic)
