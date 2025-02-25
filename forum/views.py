from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, PersonalNotes
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required


def homePageView(request):
    # The session of the current user is deleted
    # to fix Broken Access Control:
    try:
        del request.session["user"]
    except KeyError:
        return render(request, 'index.html')
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

        # Hash password before adding it to database:
        hashed_password = make_password(password)

        User.objects.create(username=username, password=hashed_password)
        return redirect("/")
    

    
    return redirect("/")

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")


    db_password = User.objects.filter(username=username).values()

    db_password = db_password.all()[0]["password"]

    if check_password(password, db_password):

        context = {"username": password}

        request.session["user"] = f"{username}"

        return render(request, "home.html", context)
    
    else:
        #luo laskuri, montako kretaa kokeiltu. session[lsekuri]. jos kolmesti,
        #estä pääsy! tääm on bruteforce hyökkäyksen esto!
        pass

    return redirect("/")


def notes(request):
    username = request.session["user"]

    notes = PersonalNotes.objects.filter(username=username)

    context = {"notes": notes}

    return render(request, "notes.html", context)

def addNote(request):

    username = request.session["user"]

    note = request.POST.get("content")

    PersonalNotes.objects.create(username=username, note=note)

    return redirect("/notes")