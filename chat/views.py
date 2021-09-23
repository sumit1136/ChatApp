from django.shortcuts import render,redirect
from django.contrib import messages


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request,"Login required")
        return redirect('signin')
    return render(request, 'chat/index.html',{})

def room(request, room_name):
    if not request.user.is_authenticated:
        messages.error(request,"Login required")
        return redirect('login')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
    })

    