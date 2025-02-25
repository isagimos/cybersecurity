from django.urls import path

from .views import homePageView, signUpView, addUser, login, notes, addNote, accessDenied

urlpatterns = [
    path('', homePageView, name='home'),
    path('signup/', signUpView, name='signup'),
    path('adduser/', addUser, name='adduser'),
    path('login/', login, name='login'),
    path('notes/', notes, name='notes'),
    path('notes/<int:tid>', notes, name='notes'),
    path('addnote/', addNote, name='addnote'),
    path('login/access_denied/', accessDenied, name='access_denied'),
   # path('addmessage/', addMessage, name='addmessage'),
]