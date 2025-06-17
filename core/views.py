from django.shortcuts import render

def index(request):
    context = {
        'curso': 'programa blablabla'
    }
    return render(request,"index.html", context)

def login(request):
    return render(request, "login.html")