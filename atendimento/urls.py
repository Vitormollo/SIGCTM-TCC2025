from django.urls import path
from . import views  # Corrigido para importar views do app atendimento

urlpatterns = [
    path('', views.atendimento, name='atendimento'),
]
