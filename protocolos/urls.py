from django.urls import path
from . import views

urlpatterns = [
    path('', views.protocolos, name='protocolos'),
]
