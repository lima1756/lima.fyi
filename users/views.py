from django.shortcuts import render, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def user_control(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')