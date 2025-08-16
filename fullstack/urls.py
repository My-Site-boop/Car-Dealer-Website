"""
URL configuration for fullstack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from fullstack import views
from members.views import home,en,home1

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', home, name="homes"),   #it is call by members(app) ke views se
     path('home1/', home1),  #it is call by fullstack ke views se
     path('home2/', views.home2),   #it is call by fullstack ke views se
     path('en/', en, name="enqury"),  #it is call by members(app) ke views se


]
