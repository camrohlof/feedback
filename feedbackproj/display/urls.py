from django.urls import path

from . import views

app_name = "display"

urlpatterns = [
    path("", view=views.HomeView.as_view(), name="event_list"),
    path("events.html", view=views.EventView.as_view(), name="events"),
]
