from django.contrib import admin

# Register your models here.
from .models import AssistidoTeste, Cliente


admin.site.register(AssistidoTeste)
admin.site.register(Cliente)