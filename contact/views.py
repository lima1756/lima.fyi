from django.shortcuts import render, redirect
from django.http import Http404
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.
def index(request):
    form = ContactForm()
    context = {
        'form': form
    }
    print(form.description)
    return render(request, 'contact/index.html', context)

def send(request):
    if request.POST:
        form = ContactForm(request.POST)
        contact_data = form.save()
        send_mail(
            contact_data.name,
            contact_data.message,
            contact_data.email,
            ['luisivanmorett@gmail.com']
        )
        return redirect('contact:index')
    raise Http404


