from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Room,Message
from datetime import  datetime,timedelta

# Create your views here.

@login_required
def rooms(request):
    # deleting all moessages older than 24 hours
    Message.objects.filter(date_added__lt=datetime.now()-timedelta(days=1)).delete()

    # delteting all rooms older than a week
    Room.objects.filter(date_added__lt=datetime.now()-timedelta(days=7)).delete()

    rooms = Room.objects.all()
    return render(request,'room/rooms.html',{"rooms":rooms})

@login_required
def room(request,slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request,'room/room.html',{"room":room,"messages":messages})

@login_required
def create_room(request):
    if request.method == "POST":
        roomname = request.POST['roomname']
        slug = roomname.lower()
        try:
            room = Room.objects.create(name=roomname,slug=slug)
            room.save()
        except:
            rooms = Room.objects.all()
            return render(request, "room/rooms.html", {
                "message": "uh uhhhhh have to be unique.",
                "rooms":rooms
            })
        return HttpResponseRedirect(reverse('rooms'))
    else:
        return HttpResponseRedirect(reverse("rooms"))
