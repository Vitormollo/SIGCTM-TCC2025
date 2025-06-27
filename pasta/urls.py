from django.urls import path
from . import views

urlpatterns = [
    path('', views.pasta_view, name='assistidos'),
    path('pasta/', views.pasta_view, name='pasta'),
]