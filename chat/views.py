# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name, nickname):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'nickname': nickname
    })