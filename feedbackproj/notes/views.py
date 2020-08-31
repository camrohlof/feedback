from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Comment, Note

# Create your views here.


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["forDate", "subject", "summary", "details"]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(NoteCreateView, self).get_form(form_class)
        form.fields["forDate"].widget = forms.DateInput(attrs={"type": "date"})
        return form


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ["forDate", "subject", "summary", "details"]
    action = "Update"

    def get_form(self, form_class=None):
        form = super(NoteUpdateView, self).get_form(form_class)
        form.fields["forDate"].widget = forms.DateInput(attrs={"type": "date"})
        return form


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("notes:list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["note", "body"]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        note = get_object_or_404(Note, slug=self.kwargs.get("slug"))
        return {
            "note": note,
        }

    def get_success_url(self):
        note = get_object_or_404(Note, slug=self.kwargs.get("slug"))
        return reverse("notes:detail", kwargs={"slug": note.slug})
