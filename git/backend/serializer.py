from rest_framework import serializers
from .models import Event, Message, Photo

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('titre', 'flyer', 'description')

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('nom', 'mail', 'message', 'date')

class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', 'artiste', 'date')