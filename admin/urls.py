from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/json/edit', views.edit_resume_json, name='edit_resume_json')
]