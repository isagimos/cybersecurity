from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


def homePageView(request):
    return render(request, 'index.html')

def signUpView(request):
    return render(request, 'signup.html')