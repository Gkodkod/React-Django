from django.urls import path

from .views import RoomView, GetRoom

urlpatterns = [
    path("create-room", RoomView.as_view()),
    path("get-rooms", GetRoom.as_view()),
]
