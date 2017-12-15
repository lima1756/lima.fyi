from os import path
from ivanmorett.settings import STATICFILES_DIRS
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    json = open(path.join(STATICFILES_DIRS[0], 'me.json'), encoding='utf-8').read()
    print(json)
    context = {
        'number': 5,
    }
    return render(request, 'resume/index.html', context)