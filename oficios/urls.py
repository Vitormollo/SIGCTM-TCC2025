from django.urls import path
from . import views  # Corrigido para importar views do app oficios

urlpatterns = [
    path('', views.oficios, name='oficios'),
]
