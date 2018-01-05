from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id_post>/<str:title>', views.post, name='post'),
    path('post/claps/<int:id_post>', views.ajax_claps, name='claps')
]