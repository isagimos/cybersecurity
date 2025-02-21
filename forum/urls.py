from django.urls import path

from .views import homePageView, signUpView, addUser

urlpatterns = [
    path('', homePageView, name='home'),
    path('signup/', signUpView, name='signup'),
    path('adduser/', addUser, name='adduser')
]