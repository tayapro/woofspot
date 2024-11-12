from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import WoofspotEvent

# Create your views here.
class FetchEvents(generic.ListView):
    queryset = WoofspotEvent.objects.all()
    template_name = "event_app/index.html"
    context_object_name = "events"
    paginate_by = 6


def get_event(request, slug):
    queryset = WoofspotEvent.objects.all()
    event = get_object_or_404(queryset, slug=slug)
    return render(request, "event_app/event_info.html", {"event": event},)

