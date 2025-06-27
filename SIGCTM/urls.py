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
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),




    path('', views.home_view, name='home'),




    path('usuarios/', include('usuario.urls')),  # login e logout

    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    path('atendimento/', views.atendimento, name='atendimento'),


    path('assistidos/', include('pasta.urls')),
    path('notificacao/', include('notificacao.urls')),
    path('atividade/', include('log.urls')),
    path('oficios/', include('oficios.urls')),
    path('pasta/', include('pasta.urls')),

    
    path('protocolos/', views.protocolos, name='protocolos'),
    path('atividade/', views.atividade, name='atividade'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    
]
