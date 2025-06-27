from django.shortcuts import render

def backup_view(request):
    return render(request, 'backup/backup.html', {'pagina_atual': 'backup'})
