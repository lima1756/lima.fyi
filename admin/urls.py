from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/json/edit', views.edit_resume_json, name='edit_resume_json'),
    path('resume/log', views.log_resume, name='log_resume'),
    path('resume/ajax/get', views.ajax_get_resume, name='ajax_get_resume'),
    path('resume/revert', views.revert_resume, name='revert_resume'),
    path('blog/posts', views.blog_posts, name='blog_posts'),
    path('blog/post/<int:id_post>', views.blog_post, name='blog_post'),
    path('blog/new/post', views.blog_post, name='blog_new_post'),
    path('blog/save/post', views.blog_post_save, name='save_post'),
    path('portfolio/', views.portfolio_index, name='portfolio'),
    path('portfolio/project/<int:id_project>', views.portfolio_project, name='portfolio_project'),
    path('portfolio/new/project', views.portfolio_project, name='portfolio_new_project'),
    path('portfolio/save/project', views.portfolio_project_save, name='save_project'),
]