from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'usuario/login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'usuario/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('usuario:login')
    

# Create your views here.
