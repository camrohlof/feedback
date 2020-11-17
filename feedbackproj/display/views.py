from datetime import datetime

from django.views.generic import ListView, TemplateView

from .models import Event

# Create your views here.


class HomeView(TemplateView):
    template_name = "display/event_list.html"


class EventView(ListView):
    model = Event
    template_name = "display/events.html"
    context_object_name = "current_events"

    def get_queryset(self):
        timeBefore = datetime.now() + datetime.timedelta(hours=-1)
        timeAfter = datetime.now() + datetime.timedelta(hours=2)
        queryset = Event.objects.all()
        queryset = queryset.order_by("dayTime")
        queryset = queryset.filter(dayTime__range=(timeBefore, timeAfter))[:5]
        return queryset
