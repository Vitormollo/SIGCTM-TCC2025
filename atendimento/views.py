from django.shortcuts import render

def atendimento(request):
    return render(request, 'atendimento/atendimento.html', {'pagina_atual': 'atendimento'})
