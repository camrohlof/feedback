from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


# Create your models here.
class Note(TimeStampedModel):
    subject = models.CharField("Subject of Note", max_length=255)
    slug = AutoSlugField(
        "Note Address", unique=True, always_update=False, populate_from="subject"
    )
    summary = models.TextField("Summary", blank=True)
    details = models.TextField("Details", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.created.strftime("%c") + " - " + self.subject

    def get_absolute_url(self):
        return reverse("notes:detail", kwargs={"slug": self.slug})


class Comment(TimeStampedModel):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="comments")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    body = models.TextField()

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
