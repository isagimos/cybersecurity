from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


def homePageView(request):
    return render(request, 'index.html')

def signUpView(request):
    return render(request, 'signup.html')

def addUser(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    password2 = request.POST.get("password2")

    # Make sure the passowrds match:
    if password != password2:
        return redirect("/signup")

    # Make sure the username is unique:
    try:
        test_username = User.objects.get(username=username)
    except:

        # Make sure the password is at least 8 characters:
        if len(password) <= 8:
            return redirect("/signup")

        User.objects.create(username=username, password=password)
        return redirect("/")
    

    
    return redirect("/")