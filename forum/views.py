from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Notes
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
import time


def homePageView(request):

    # FLAW 4: Security Logging and Monitoring Failure.
    # There is no checking if the access is denied or not:
    
#   if check(request) == False:
#       return redirect("login/access_denied/")

    # FLAW 3: Broken Access Control.
    # The session of the current user should be deleted upon logout:
    
#   try:
#       del request.session["user"]
#   except KeyError:
#       return render(request, 'index.html')
    
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

        # FLAW 1: Insecure Design.
        # Without the following code the length of the password is not checked:
        
#       if len(password) <= 8:
#           return redirect("/signup")
        
        # FLAW 2: Cryptographic Failures.
        # Without the following code the password is not hashed before adding it to database:
        
#       password = make_password(password)

        User.objects.create(username=username, password=password)
        return redirect("/")
    

    
    return redirect("/")

def login(request):
    
    # FLAW 4: Security Logging and Monitoring Failure.
    # There is no checking if the access is denied or not:
    
#   if check(request) == False:
#       return redirect("login/access_denied/")
        
    username = request.POST.get("username")
    password = request.POST.get("password")

    try:
        db_password = User.objects.filter(username=username).values()

        db_password = db_password.all()[0]["password"]

        if check_password(password, db_password):

            request.session["user"] = f"{username}"

            return render(request, "home.html")
    except:
        pass

    # FLAW 4: Security Logging and Monitoring Failures.
    # request.session["tries"] should be monitoring login attempts.
    # If somebody gives an incorrect password more than 3 times
    # the user is redirected to "access_denied/":
    
#   try:
#       request.session["tries"] += 1
#   except:
#       request.session["tries"] = 1
    
#   if request.session["tries"] > 3:

#       x = time.time()

#       request.session["lock"] = x

#       return redirect("access_denied/")

    return redirect("/")

def notes(request):
    username = request.session["user"]

    notes = Notes.objects.all()

    context = {"notes": notes}

    return render(request, "notes.html", context)


def addNote(request):

    note = request.POST.get("content")

    # FLAW 5: Injection and Cross-Site Scripting.
    # XSS vulnerability. Without the following, the <'s and >'s are not replaced by
    # HTML character entities &lt; and &gt; (less than and greater than)
    # before the message is saved to the database. Because of this, a possible
    # HTML code is rendered when notes.html is rendered to the user:
    
#   note = note.replace("<", "&lt;").replace(">", "&gt;")

    # Without checking the username the application is vulnerable to attacks:
#   username = request.session["user"]

#   Notes.objects.create(username=username, note=note)
    # The previous row would make sure that username is required when saving messages to the database.
    # Without this requirement the application is more vulnerable to CSRF attack:
    Notes.objects.create(note=note)

    return redirect("/notes")

def accessDenied(request):

    request.session["tries"] = 0

    x = request.session["lock"]

    y = time.time()

    if y - x < 60:
        return render(request, "access_denied.html")
    
# Check if 60 seconds has passed and the user is allowed
# to try to log in again:
def check(request):
    y = time.time()

    try:
        x = request.session["lock"]
    except:
        return True
    
    if y - x < 60:
        return False

    return True
