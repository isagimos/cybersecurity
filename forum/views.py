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

    User.objects.create(username=username, password=password)

    return redirect("/")