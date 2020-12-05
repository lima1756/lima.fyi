"""ivanmorett URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls.static import static
import ivanmorett.settings as settings

urlpatterns = [
    path('', include(('resume.urls', 'resume'), namespace='resume')),
    path('admin/', include(('admin.urls', 'admin'), namespace='admin')),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('portfolio/', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('base_conversor/', include(('base_conversor.urls', 'base_conversor'), namespace='base_conversor')),
    path('base_converter/', include(('base_conversor.urls', 'base_converter'), namespace='base_covnerter')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
