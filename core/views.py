from django.shortcuts import render
from django.http import HttpResponse
from .models import usuarios

# Create your views here.
def core(request):
    return render(request,'index.html')