from django.urls import path

from .views import homePageView, signUpView, addUser, login, notes, addNote

urlpatterns = [
    path('', homePageView, name='home'),
    path('signup/', signUpView, name='signup'),
    path('adduser/', addUser, name='adduser'),
    path('login/', login, name='login'),
    path('notes/', notes, name='notes'),
    path('notes/<int:tid>', notes, name='notes'),
    path('addnote/', addNote, name='addnote'),
    path('accounts/login', login, name="login")
]