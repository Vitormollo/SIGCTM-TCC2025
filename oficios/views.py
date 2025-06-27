from django.shortcuts import render

def oficios(request):
    return render(request, 'oficios/oficios.html', {'pagina_atual': 'oficios'})
