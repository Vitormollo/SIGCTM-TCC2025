from django.urls import path

from .views import index, login

urlpatterns = [
    path('',index),
    path('login',login),
]