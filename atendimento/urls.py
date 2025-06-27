from django.urls import path
from core import views  # enquanto as views ainda estiverem no core

urlpatterns = [
    path('', views.atendimento, name='atendimento'),
]
