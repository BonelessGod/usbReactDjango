from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializer import eventSerializer, messageSerializer, photoSerializer
from .models import Event, Photo

class EventView(viewsets.ModelViewSet):
    serializer_class = eventSerializer
    queryset = Event.objects.all()

class PhotoView(viewsets.ModelViewSet):
    serializer_class = photoSerializer
    queryset = Photo.objects.all()

@api_view(['POST'])
@permission_classes([AllowAny])
def MessageView(request):
    serializer = messageSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)