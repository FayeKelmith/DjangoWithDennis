from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

rooms = [
    {"id":1, "name": "Let's code"},
    {"id":2, "name": "Django is kinda dope"},
    {"id":3, "name": "Except templates"},
         ]

def home(request):
    return render(request, 'home.html',{'rooms':rooms})


def room(request):
    return render(request, 'room.html')
    