from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})