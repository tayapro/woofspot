"""
URL configuration for woofspot_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import render
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf.urls.static import static
from . import views

handler400 = 'woofspot_project.views.custom_400'
handler403 = 'woofspot_project.views.custom_403'
handler404 = 'woofspot_project.views.custom_404'
handler500 = 'woofspot_project.views.custom_500'


# URL patterns
urlpatterns = [
    # Django-Browser-Reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Admin interface
    path("admin/", admin.site.urls),
    # Summernote WYSIWYG editor
    path("summernote/", include("django_summernote.urls")),
    # Custom overrides for customized allauth features in user_app
    path("", include("user_app.urls")),
    # User authentication via Django Allauth
    path("accounts/", include("allauth.urls")),
    # Event app (root URL)
    path("", include("event_app.urls"), name="event-app-urls"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
