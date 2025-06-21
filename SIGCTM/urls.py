"""
URL configuration for SIGCTM project.

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

from core import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('assistidos/', views.assistidos, name='assistidos'),
    path('atendimento/', views.atendimento, name='atendimento'),
    path('notificacao/', views.notificacao, name='notificacao'),
    path('oficios/', views.oficios, name='oficios'),
    path('protocolos/', views.protocolos, name='protocolos'),
    path('atividade/', views.atividade, name='atividade'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
]
