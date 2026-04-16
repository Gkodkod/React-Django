from django.urls import path

from .views import main

urlpatterns = [
    ## multiple paths to the same view
    path("", main),
    path("home", main),
]
