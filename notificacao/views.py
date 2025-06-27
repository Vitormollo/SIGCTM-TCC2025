from django.shortcuts import render

def notificacao(request):
    return render(request, 'notificacao/notificacao.html')