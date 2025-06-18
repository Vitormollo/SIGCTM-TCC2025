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
    return render(request, 'index.html')

def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
