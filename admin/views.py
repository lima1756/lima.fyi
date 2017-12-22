from os import path
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    context = {
        
    }
    return render(request, 'admin/base.html', context)

def dashboard(request):
    pass