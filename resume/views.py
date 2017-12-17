import json

from os import path
from ivanmorett.settings import STATICFILES_DIRS
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    data = open(path.join(STATICFILES_DIRS[0], 'me.json'), encoding='utf-8').read()
    decoded_json = json.loads(data)
    aptitudes_categories = []
    for apt in decoded_json['aptitudes']:
        if apt['type'] not in aptitudes_categories:
            aptitudes_categories.append(apt['type'])
    print(aptitudes_categories)
    aptitudes_categories_grid = 12//len(aptitudes_categories)
    aptitudes_categories_grid = aptitudes_categories_grid if aptitudes_categories_grid >= 3 else 3
    awards_grid = 12//len(decoded_json['awards'])
    awards_grid = awards_grid if awards_grid >= 4 else 4
    context = {
        'data': decoded_json,
        'aptitudes_categories': aptitudes_categories,
        'aptitudes_categories_grid': aptitudes_categories_grid,
        'awards_grid': awards_grid
    }
    return render(request, 'resume/index.html', context)