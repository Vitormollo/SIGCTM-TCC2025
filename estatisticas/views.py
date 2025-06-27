from django.shortcuts import render

def estatisticas(request):
    return render(request, 'estatisticas/estatisticas.html', {'pagina_atual': 'estatisticas'})
