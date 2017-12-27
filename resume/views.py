import json

from os import path
from ivanmorett.settings import STATICFILES_DIRS
from django.shortcuts import render
from django.template import loader
from admin.models import ResumeLog
# Create your views here.


def index(request):
    data = json.loads(ResumeLog.objects.latest('date_time_edited').resume)
    aptitudes_categories = []
    for apt in data['aptitudes']:
        if apt['type'] not in aptitudes_categories:
            aptitudes_categories.append(apt['type'])
    aptitudes_categories_grid = 12//len(aptitudes_categories)
    aptitudes_categories_grid = aptitudes_categories_grid if aptitudes_categories_grid >= 3 else 3
    awards_grid = 12//len(data['awards'])
    awards_grid = awards_grid if awards_grid >= 4 else 4
    context = {
        'data': data,
        'aptitudes_categories': aptitudes_categories,
        'aptitudes_categories_grid': aptitudes_categories_grid,
        'awards_grid': awards_grid
    }
    return render(request, 'resume/index.html', context)