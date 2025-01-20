"""
URL configuration for woofspot_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import render
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf.urls.static import static
from . import views


# Custom handler for Bad Request errors (400)
handler400 = 'woofspot_project.views.custom_400'
# Custom handler for Forbidden errors (403)
handler403 = 'woofspot_project.views.custom_403'
# Custom handler for Page Not Found errors (404)
handler404 = 'woofspot_project.views.custom_404'
# Custom handler for Server Error (500)
handler500 = 'woofspot_project.views.custom_500'

# URL patterns for the project
urlpatterns = [
    # Admin interface
    path("admin/", admin.site.urls),

    # Summernote WYSIWYG editor
    path("summernote/", include("django_summernote.urls")),

    # User authentication and management
    # Includes custom overrides for Django Allauth features
    path("", include("user_app.urls")),
    # Adds authentication functionalities (e.g., login, logout)
    path("accounts/", include("allauth.urls")),  

    # Routes for event-related views
    path("", include("event_app.urls"), name="event-app-urls"),
]
