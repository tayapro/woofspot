from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from event_app.models import WoofspotEvent

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactUsForm

def contact_us_form_submit(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            comment = form.cleaned_data["comment"]

            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{comment}",
                from_email=email,
                recipient_list=["woofspot.app@gmail.com"],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request, "There was an error in your submission. Please try again.")

    return render(request, "base.html", {"form": ContactUsForm()})


@login_required
def profile(request):
    user = request.user
    next = request.GET.get('next', '/')

    return render(request, "user_app/profile.html", 
    {
        "next": next,
        "user": user,
    })
