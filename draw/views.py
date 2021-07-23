# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def home(request):
    return render(request, 'draw/home.html')

def search1(request):
    return render(request, 'draw/search1.html')

def search2(request):
    return render(request, 'draw/search2.html')

def info(request):
    return render(request, 'draw/info.html')
