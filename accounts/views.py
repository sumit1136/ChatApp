from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import random


c=0

def signup(request):
    global c
    if(request.method=="POST"):
        username = request.POST.get('username')
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
        if(password and password2 and password == password2):
            user = User.objects.create_user(username=username, password=password)
            user.save()
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
    if(request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if(user is not None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('signin')

    else:
        return render(request,"accounts/login.html")

