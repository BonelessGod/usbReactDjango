from django.contrib import admin
from backend.models import Event, Message, Photo

class EventAdmin(admin.ModelAdmin):
    list = ('titre', 'flyer', 'description')

class MessageAdmin(admin.ModelAdmin):
    list = ('nom', 'mail', 'message', 'date')

class PhotoAdmin(admin.ModelAdmin):
    list = ('image', 'artiste', 'date')

admin.site.register(Event, EventAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Photo, PhotoAdmin)
