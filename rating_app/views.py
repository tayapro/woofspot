from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Rating
from .forms import RatingForm
from event_app.models import WoofspotEvent


def rate_create(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == 'POST':
        rating_form = RatingForm(request.POST, event=event)
        
        if rating_form.is_valid():
            try:
                rating_form.save(user=request.user)
                return redirect("event_app:event_view", slug=event.slug)
            except IntegrityError:
                raise IntegrityError("You have already rated this event.")
        else:
            raise ValidationError("There was an error with your form submission.")
    else:
        rating_form = RatingForm(event=event)
    
    return render(request, "rate_event.html", {"form": rating_form, "event": event})