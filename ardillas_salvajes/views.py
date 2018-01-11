from django.shortcuts import render, redirect, reverse
from django.http import Http404
from django.core.mail import send_mail
from .forms import ContactForm, CommentForm
from .models import Comment

def index(request):
    contact_form = ContactForm()
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'contact_form': contact_form,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'ardillas_salvajes/index.html', context)

def comment(request):
    if request.POST:
        form = CommentForm(request.POST)
        contact = form.save()
        return redirect('ardillas_salvajes:index')
    raise Http404


def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        contact = form.save()
        message= contact.name + ' said: ' + contact.content
        send_mail(
            'Nuevo mensaje desde ardillas_salvajes',
            message,
            contact.email,
            ['luisivanmorett@gmail.com']
        )
        send_mail(
            'Copia de mensaje enviado a ardillas_salvajes',
            message,
            'ardillas_salvajes@ivanmorett.com',
            [contact.email]
        )
        url = reverse('ardillas_salvajes:index')
        return redirect(url+'?saved=true')
    raise Http404