from django.shortcuts import render

def assistido_view(request):
    return render(request, 'assistido/assistidos.html', {'pagina_atual': 'assistidos'})
