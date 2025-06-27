from django.shortcuts import render

def pasta_view(request):
    return render(request, 'assistidos.html', {'pagina_atual': 'assistidos'})
