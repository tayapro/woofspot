from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("contact-us/", views.contact_us_form_submit, name="contact_form_submit"),
]