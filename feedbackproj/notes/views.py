from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Note

# Create your views here.


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["subject", "summary", "details"]
    login_url = "/login/"
    redirect_field_name = "redirect_to"


class NoteUpdateView(UpdateView):
    model = Note
    fields = ["subject", "summary", "details"]
    action = "Update"
    template_name_suffix = "_update"
