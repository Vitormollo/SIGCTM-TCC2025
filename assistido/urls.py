from django.urls import path
from . import views

urlpatterns = [
    path('', views.assistido_view, name='assistidos'),
    path('assistido/', views.assistido_view, name='assistido'),
]
