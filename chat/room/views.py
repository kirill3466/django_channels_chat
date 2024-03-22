from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(
        request, 'room/room.html', {'room': room, 'messages': messages}
    )


@login_required
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
    return render(request, 'room/create_room.html')
