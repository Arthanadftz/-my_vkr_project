"""newspaper_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic.base import TemplateView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('pages.urls')),
    path('articles/', include('articles.urls')),
    path('orders/', include('orders.urls')),
    path('chat/', include('chat.urls')),
    path('attendance/', include('attendance_control.urls')),
    path('admin/', admin.site.urls, name='admin_page'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
