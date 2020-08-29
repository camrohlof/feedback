from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path(route="", view=views.NoteListView.as_view(), name="list"),
]
