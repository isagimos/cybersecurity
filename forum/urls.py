from django.urls import path

from .views import homePageView, signUpView

urlpatterns = [
    path('', homePageView, name='home'),
    path('signup/', signUpView, name='signup')
]