from os import path
from datetime import datetime
from ivanmorett.settings import STATICFILES_DIRS
from django.shortcuts import render, Http404, redirect, reverse
from django.template import loader
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import ResumeLogForm, PostForm
from .models import ResumeLog
from blog.models import Post, Tag


def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser)
def index(request):
    context = {
    
    }
    return render(request, 'admin/dashboard.html', context)

    
@user_passes_test(is_superuser)
def edit_resume_json(request):    
    if request.method == 'POST':
        modelData = ResumeLogForm(request.POST)
        commit = modelData.save()
        data = commit.resume
        return redirect('edit_resume_json')
    try:
        data = ResumeLog.objects.latest('date_time_edited').resume
    except ObjectDoesNotExist:
        data = open(path.join(STATICFILES_DIRS[0], 'me.json'), encoding='utf-8').read()
        new_title = 'Resume Template'
        new_description = 'This is the initial automatic resume template.'
        resume_log = ResumeLog(title=new_title,
                               description=new_description,
                               resume=data)
        resume_log.save()
    except MultipleObjectsReturned:
        data = '{"error":"There is an error with the database"}'
    form = ResumeLogForm()
    context = {
        'json_data': data if len(data)>0 else None,
        'form': form,
    }
    return render(request, 'admin/edit_resume_json.html', context)


@user_passes_test(is_superuser)
def log_resume(request):
    resume_logs = ResumeLog.objects.all()
    paginator = Paginator(resume_logs, 5)
    page = request.GET.get('page')
    resumes = paginator.get_page(page)
    min_page = resumes.number - 5
    max_page = resumes.number + 5 + (0 if min_page > -1 else -min_page)
    min_page = 1 if min_page < 1 else min_page
    max_page = max_page if max_page <= paginator.num_pages else paginator.num_pages
    context = {
        "resume_logs": resumes,
        'pages': [i for i in range(min_page, max_page+1)],
    }
    return render(request, 'admin/log_resume.html', context)

@user_passes_test(is_superuser)
def ajax_get_resume(request):
    if request.POST:
        resume = ResumeLog.objects.get(id=request.POST['id'])
        data={
            'title': resume.__str__(),
            'resume':resume.resume
        }
        return JsonResponse(data)
    else:
        raise Http404


@user_passes_test(is_superuser)
def revert_resume(request):
    if request.POST:
        resume_to_revert = ResumeLog.objects.get(id=request.POST['id'])
        new_title = 'REVERTED TO: ' + str(resume_to_revert)
        new_description = ('<strong>Original date-time: </strong>' +\
                        str(resume_to_revert.date_time_edited) +\
                        '<br><strong>The original title was: </strong>' +\
                        resume_to_revert.title +\
                        '<br><strong> The original description was: </strong>' +\
                        resume_to_revert.description +\
                        '<br><strong> Rverted on: </strong>' +\
                        str(datetime.now())
                        )
        resume_log = ResumeLog(title=new_title,
                               description=new_description,
                               resume=resume_to_revert.resume)
        resume_log.save()
        return redirect('log_resume')
    else:
        raise Http404


@user_passes_test(is_superuser)
def blog_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'admin/blog_posts.html', context)


@user_passes_test(is_superuser)
def blog_post(request, id_post=None):
    try:
        post = Post.objects.get(id=id_post) if id_post else None
    except ObjectDoesNotExist:
        return redirect('blog_new_post')
    saved = True if request.GET else False
    form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
        'saved': saved
    }
    return render(request, 'admin/blog_post.html', context)


@user_passes_test(is_superuser)
def blog_post_save(request):
    if request.POST:
        id = request.POST['id'] if request.POST['id'] != '' else None
        title = request.POST['title']
        content = request.POST['content'].replace('"', '\"')
        date = request.POST['date_published'] if request.POST['date_published'] != '' else None
        visible = True if 'visible' in request.POST else False
        tags =  request.POST.getlist('tags')
        for i in range(len(tags)):
            if not tags[i].isnumeric():
                tag = Tag(name=tags[i])
                tag.save()
                tags[i] = tag.id
            else:
                tags[i] = int(tags[i])
        if id:
            post = Post.objects.get(id=id)
            post.title = title
            post.content = content
            post.visible = visible
            post.date_published = date
        else:
            post = Post(title=title, content=content, visible=visible, date_published=date)
        post.save()
        post.tags.set(tags)
        url = reverse('admin:blog_post',kwargs={'id_post':post.id})
        return redirect(url+'?saved=true')
    raise Http404
    
    