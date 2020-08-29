from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Note

# Create your views here.


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(CreateView):
    model = Note
    fields = ["subject", "summary", "details"]


class NoteUpdateView(UpdateView):
    model = Note
    fields = ["subject", "summary", "details"]
    action = "Update"
    template_name_suffix = "_update"
