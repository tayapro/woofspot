from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .models import WoofspotEvent


class FetchEvents(generic.ListView):
    queryset = WoofspotEvent.objects.all()
    template_name = "index.html"
    context_object_name = "events"
    paginate_by = 6


def event_detail(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == 'POST' and 'reserve_spot' in request.POST:
        if request.user.is_authenticated:
            if request.user in event.attendees.all():
                messages.error(request, "You have already reserved a spot for this event.")
            else:
                event.attendees.add(request.user)
                messages.success(request, "Slot is reserved!")
        else:
            return redirect(f"{reverse('signin')}?next={request.path}")

    user_registered = (
        request.user.is_authenticated and request.user in event.attendees.all()
    )
    return render(request, "event_info.html", 
                 {"event": event, 
                 "user_registered": user_registered}
                 )


def events_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('my_signin'))
    events = WoofspotEvent.objects.filter(attendees=request.user) 

    return render(request, "events.html",
    {
        "user": user,
        "events": events,
    })

def cancel_event_page(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('my_signin'))

    if request.method == 'POST' and 'cancel_reservation' in request.POST:  
        event = get_object_or_404(WoofspotEvent, slug=slug)
        event.attendees.remove(request.user)
        return redirect(reverse('events'))
        
    return render(request, "cancel_event.html",
    {
        "slug": slug,
        "user": user,
    })