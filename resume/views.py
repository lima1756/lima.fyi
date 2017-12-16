import json

from os import path
from ivanmorett.settings import STATICFILES_DIRS
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    data = open(path.join(STATICFILES_DIRS[0], 'me.json'), encoding='utf-8').read()
    decoded_json = json.loads(data)
    print(decoded_json['personal_data'])
    context = {
        'data': decoded_json,
    }
    return render(request, 'resume/index.html', context)