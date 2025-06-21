from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.http import HttpResponse
from .models import usuarios

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Pega o checkbox

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Se o usuário NÃO marcar "Lembre-se de mim", a sessão expira ao fechar o navegador
            if not remember_me:
                request.session.set_expiry(0)  # Expira ao fechar navegador
            else:
                # Se marcar, dura por exemplo 30 dias
                request.session.set_expiry(timedelta(days=365))

            return redirect('dashboard')
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, 'login.html')

def logout_view(request):
    django_logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'index.html', {'pagina_atual': 'dashboard'})

@login_required(login_url='login')
def assistidos(request):
    return render(request, 'assistidos.html', {'pagina_atual': 'assistidos'})

@login_required(login_url='login')
def atendimento(request):
    return render(request, 'atendimento.html', {'pagina_atual': 'atendimento'})

@login_required(login_url='login')
def notificacao(request):
    return render(request, 'notificacao.html', {'pagina_atual': 'notificacao'})

@login_required(login_url='login')
def oficios(request):
    return render(request, 'oficios.html', {'pagina_atual': 'oficios'})

@login_required(login_url='login')
def protocolos(request):
    return render(request, 'protocolos.html', {'pagina_atual': 'protocolos'})

@login_required(login_url='login')
def atividade(request):
    return render(request, 'atividade.html', {'pagina_atual': 'atividade'})

@login_required(login_url='login')
def estatisticas(request):
    return render(request, 'estatisticas.html', {'pagina_atual': 'estatisticas'})


def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
    



