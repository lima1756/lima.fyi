from django.shortcuts import render
from .models import Project
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    projects = Project.objects.filter(visible=True)
    context = {
        'projects':projects
    }
    return render(request, 'portfolio/index.html', context)


def project(request, id_project, name):
    project = Project.objects.get(id=id_project)
    context = {
        'project':project
    }
    return render(request, 'portfolio/project.html', context)