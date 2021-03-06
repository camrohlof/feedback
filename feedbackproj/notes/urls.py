from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path(route="", view=views.NoteListView.as_view(), name="list"),
    path(route="add/", view=views.NoteCreateView.as_view(), name="add"),
    path(
        route="<slug:slug>/addcomment/",
        view=views.CommentCreateView.as_view(),
        name="addcomment",
    ),
    path(
        route="<slug:slug>/delete/", view=views.NoteDeleteView.as_view(), name="delete"
    ),
    path(
        route="<slug:slug>/update/", view=views.NoteUpdateView.as_view(), name="update"
    ),
    path(route="<slug:slug>/", view=views.NoteDetailView.as_view(), name="detail"),
]
