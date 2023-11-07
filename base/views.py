from django.shortcuts import render
from django.http import HttpResponse

from .models import Room
# Create your views here.

rooms = [
    {"id":1, "name": "Let's code"},
    {"id":2, "name": "Django is kinda dope"},
    {"id":3, "name": "Except templates"},
         ]
 
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)


def room(request,pk):
    context = {'id':[{"id":pk}]}
    return render(request, 'base/room.html',context)
    