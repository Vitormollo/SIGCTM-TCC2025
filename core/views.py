from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import timedelta
from .models import usuarios


def is_conselheira(user):
    return user.groups.filter(name='Conselheira').exists()


def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('usuario:login')


def dashboard_view(request):
    return render(request, 'index.html', {'pagina_atual': 'dashboard'})


def assistidos(request):
    return render(request, 'assistidos.html', {'pagina_atual': 'assistidos'})


def atendimento(request):
    return render(request, 'atendimento.html', {'pagina_atual': 'atendimento'})


def notificacao(request):
    return render(request, 'notificacao.html', {'pagina_atual': 'notificacao'})


def oficios(request):
    return render(request, 'oficios.html', {'pagina_atual': 'oficios'})


def protocolos(request):
    return render(request, 'protocolos.html', {'pagina_atual': 'protocolos'})


def atividade(request):
    return render(request, 'atividade.html', {'pagina_atual': 'atividade'})


def estatisticas(request):
    return render(request, 'estatisticas.html', {'pagina_atual': 'estatisticas'})

