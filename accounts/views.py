from django.contrib import messages
from django.core import paginator
from django.db.models import Q
from django.core.paginator import Paginator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . import models
import random


c=0

def signup(request):
    if request.user.is_authenticated:
        messages.error(request,"Already logged in")
        return redirect('profile')      
    global c
    if(request.method=="POST"):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        d=request.POST.get('c')
        
        if(User.objects.filter(username=username).exists()):
            print("username already taken")
            messages.info(request,"username already taken")
            return redirect('signup')
        
        if(d and c!=int(d)):
            messages.info(request,"Incorrect captcha")
            return redirect('signup')
        if(len(password)<8):
            messages.info(request,"Password should at least 8 characters")
            return redirect('signup')
            
        if(not password.isalnum()):
            messages.info(request,"Password should be alphanumeric")
            return redirect('signup')

        if(password and password2 and password == password2):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            models.register_table(user)
            
            print("User created")
            messages.info(request,"User created successfully")
            return redirect('signin')
        else:
            messages.info(request,"Password not matching")
            print('Password not matching')
            return redirect('signup')

    else:
        a = random.randint(1,9)
        b = random.randint(1,9)
        c=a+b
        return render(request,"accounts/register.html",{"a":a,"b":b})

def signin(request):
    if request.user.is_authenticated:
        messages.error(request,"Already logged in")
        return redirect('profile')
    if(request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if(user is not None):
            auth.login(request,user)
            return redirect('profile')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('signin')

    else:
        return render(request,"accounts/login.html")

def profile(request):
    if not request.user.is_authenticated:
        messages.error(request,"Login required")
        return redirect('signin')
    return render(request,"accounts/profile.html")

def editprofile(request):
    if not request.user.is_authenticated:
        messages.error(request,"Login required")
        return redirect('signin')
    if(request.method=="POST"):
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']

        user = User.objects.get(id=request.user.id)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()
        messages.info(request,"Editted successfully.")
    else:
        messages.info(request,None)
    return render(request,"accounts/editprofile.html")



def search(request):
    if not request.user.is_authenticated:
        messages.error(request,"Login required")
        return redirect('signin')
    if request.method=="POST":
        query = request.POST.get('q')
        if(query):
            user = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query))
            if user is not None:
                return render(request,"accounts/search.html",{"usr":user})
            else:
                messages.info(request,"No record found.")
        else:
            return redirect('search')
    return render(request,"accounts/search.html")

