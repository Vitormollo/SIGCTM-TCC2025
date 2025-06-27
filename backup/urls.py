from django.urls import path
from . import views

urlpatterns = [
    path('', views.backup_view, name='backup'),
    path('backup/', views.backup_view, name='backup'),
]
