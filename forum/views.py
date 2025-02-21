from django.http import HttpResponse
from django.shortcuts import render, redirect


def homePageView(request):
    return render(request, 'index.html')