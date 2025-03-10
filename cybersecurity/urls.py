"""
URL configuration for cybersecurity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('signup/', include('forum.urls')),
    path('login/', include('forum.urls')),
    path('notes/', include('forum.urls')),
    path('addnote/', include('forum.urls')),
    path('accounts/', include('forum.urls')),
    path('login/access_denied/', include('forum.urls')),
   # path('addmessage/', include('forum.urls')),
]