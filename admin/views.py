from os import path
from ivanmorett.settings import STATICFILES_DIRS
from django.shortcuts import render, Http404
from django.template import loader
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser)
def index(request):
    context = {
    
    }
    return render(request, 'admin/dashboard.html', context)

    
@user_passes_test(is_superuser)
def edit_resume_json(request):
    data = open(path.join(STATICFILES_DIRS[0], 'me.json'), encoding='utf-8').read()
    context = {
        'json_data': data
    }
    return render(request, 'admin/edit_resume_json.html', context)
