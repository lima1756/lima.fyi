from os import path
from datetime import datetime
from ivanmorett.settings import STATICFILES_DIRS
from django.shortcuts import render, Http404, redirect, reverse
from django.template import loader
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .forms import ResumeLogForm, PostForm, ProjectForm
from .models import ResumeLog
import blog.models as blog
import portfolio.models as portfolio


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
        return redirect('admin:edit_resume_json')
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
        return redirect('admin:log_resume')
    else:
        raise Http404


@user_passes_test(is_superuser)
def blog_posts(request):
    posts = blog.Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'admin/blog_posts.html', context)


@user_passes_test(is_superuser)
def blog_post(request, id_post=None):
    try:
        post = blog.Post.objects.get(id=id_post) if id_post else None
    except ObjectDoesNotExist:
        return redirect('admin:blog_new_post')
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
                tag = blog.Tag(name=tags[i])
                tag.save()
                tags[i] = tag.id
            else:
                tags[i] = int(tags[i])
        if id:
            post = blog.Post.objects.get(id=id)
            post.title = title
            post.content = content
            post.visible = visible
            post.date_published = date
        else:
            post = blog.Post(title=title, content=content, visible=visible, date_published=date)
        post.save()
        post.tags.set(tags)
        url = reverse('admin:blog_post',kwargs={'id_post':post.id})
        return redirect(url+'?saved=true')
    raise Http404


@user_passes_test(is_superuser)
def portfolio_index(request):
    projects = portfolio.Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'admin/portfolio.html', context)

@user_passes_test(is_superuser)
def portfolio_project(request, id_project=None):
    try:
        project = portfolio.Project.objects.get(id=id_project) if id_project else None
    except ObjectDoesNotExist:
        return redirect('admin:portfolio_new_project')
    saved = True if request.GET else False
    form = ProjectForm(instance=project)
    context = {
        'form': form,
        'project': project,
        'saved': saved
    }
    return render(request, 'admin/portfolio_project.html', context)


@user_passes_test(is_superuser)
def portfolio_project_save(request):
    if request.POST:
        post = request.POST.copy()
        tags =  request.POST.getlist('tags')
        for i in range(len(tags)):
            if not tags[i].isnumeric():
                tag = portfolio.Tag(name=tags[i])
                tag.save()
                tags[i] = tag.id
            else:
                tags[i] = int(tags[i])
        post.setlist('tags', tags)
        form = ProjectForm(post, request.FILES)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.id = request.POST['id'] if request.POST['id'] != '' else None
            saved.save()
            saved.tags.set(tags)
            saved.save()
            url = reverse('admin:portfolio_project',kwargs={'id_project':saved.id})
            return redirect(url+'?saved=true')
    raise Http404
