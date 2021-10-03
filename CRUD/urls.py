"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from django.views.decorators.cache import cache_control

from CRUD import settings
from CRUD.Apps.GestionUsuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD.Apps.GestionUsuarios.urls')),
] + static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))
handler404 = views.handler404
handler500 = views.handler500
handler403 = views.handler403