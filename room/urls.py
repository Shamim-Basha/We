from django.urls import path

from . import views

urlpatterns = [
    path("",views.rooms,name="rooms"),
    path("create",views.create_room,name="createroom"),
    path("<str:slug>",views.room,name="room")
]