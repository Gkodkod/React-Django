from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer

# Create your views here.

# API to create a room
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# API to get a room
class GetRoom(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
