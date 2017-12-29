from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/json/edit', views.edit_resume_json, name='edit_resume_json'),
    path('resume/log', views.log_resume, name='log_resume'),
    path('resume/ajax/get', views.ajax_get_resume, name='ajax_get_resume'),
    path('resume/revert', views.revert_resume, name='revert_resume'),
    path('blog/posts', views.blog_posts, name='blog_posts'),
]