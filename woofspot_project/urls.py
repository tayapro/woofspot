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
from django.conf.urls.static import static
from . import views


# Custom error handlers
def custom_404(request, exception):
    return render(request, "404.html", status=404)

def custom_500(request):
    return render(request, "500.html", status=500)

handler404 = custom_404
handler500 = custom_500


# URL patterns
urlpatterns = [
    # Admin interface
    path("admin/", admin.site.urls),
    # Summernote WYSIWYG editor
    path("summernote/", include("django_summernote.urls")),
    # Custom overrides for specific features in user_app
    path("", include("user_app.urls")),
    # User authentication via Django Allauth
    path("accounts/", include("allauth.urls")),
    # Event app (root URL)
    path("", include("event_app.urls"), name="event-app-urls"),
    # Other URL patterns
    path("trigger-500/", views.trigger_500, name="trigger-500"),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
