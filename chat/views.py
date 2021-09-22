from chat.forms import NewUserForm
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'chat/index.html',{})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

    