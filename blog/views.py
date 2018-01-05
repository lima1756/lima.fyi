from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.expressions import F
from .models import Post
from datetime import datetime, timedelta


def index(request):
    posts = Post.objects.filter(date_published__lt = datetime.now()+timedelta(days=1), visible=True)
    context = {
        'posts':posts
    }
    return render(request, 'blog/index.html', context)


def post(request, id_post, title):
    post = Post.objects.get(id=id_post)
    post.visits = F('visits') + 1
    post.save()
    post = Post.objects.get(id=id_post)
    context = {
        'post':post
    }
    return render(request, 'blog/post.html', context)



def ajax_claps(request, id_post):
    post = Post.objects.get(id=id_post)
    post.claps = F('claps') + 1
    post.save()
    post = Post.objects.get(id=id_post)
    data={
        'claps': post.claps
    }
    return JsonResponse(data)
