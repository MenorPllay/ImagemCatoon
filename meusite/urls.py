"""meusite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from cartoon import views
from cartoon.admin import admin_site

from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('myadmin/', admin_site.urls),
    path('admin/', admin.site.urls),
    path('cartoon/', views.cartoon),
    path('create', views.cartoon_submit),
    path('getprofile', views.home, name='getprofile'),
    path('delete_all_img/', views.delete_all_img, name='delete_all_img'),
    path('delete_all_img/submit', views.delete_all_img_Submit, name='delete_all_img_submit'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
