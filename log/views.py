from django.shortcuts import render

def log(request):
    return render(request, 'log/atividade.html', {'pagina_atual': 'atividade'})
