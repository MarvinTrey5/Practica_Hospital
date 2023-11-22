"""Project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app_hospital import views as appv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appv.index),
    path('meds/',appv.list_med, name='meds'),
    path('add_med/', appv.add_med,name="add_med"),
    path('pag_pacient',appv.indexP, name='pag_pacient'),
    path('add_pacient/', appv.add_pacient, name="add_pacient"),
    path('pacient/',appv.list_pacient, name='pacient'),
]
