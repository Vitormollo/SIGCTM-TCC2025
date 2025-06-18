from django.shortcuts import render
from django.http import HttpResponse
from .models import usuarios

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')