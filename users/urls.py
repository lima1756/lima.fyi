from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'users/login.html'}, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('users/', views.user_control, name='user_control'),
]