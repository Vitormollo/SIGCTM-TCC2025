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




    

    path('dashboard/', views.dashboard_view, name='dashboard'),
    

    path('usuarios/', include('usuario.urls')), 
    path('assistidos/', include('assistido.urls')),
    path('notificacao/', include('notificacao.urls')),
    path('atividade/', include('log.urls')),
    path('oficios/', include('oficios.urls')),
    path('assistido/', include('assistido.urls')),
    path('atendimento/', include('atendimento.urls')),
    path('estatisticas/', include('estatisticas.urls')),
    path('backup/', include('backup.urls')),
    path('protocolos/', include('protocolos.urls')),
    
    
    
]
