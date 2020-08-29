from autoslug import AutoSlugField
from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Note(TimeStampedModel):
    subject = models.CharField("Subject of Note", max_length=255)
    slug = AutoSlugField(
        "Note Address", unique=True, always_update=False, populate_from="subject"
    )
    summary = models.TextField("Summary", blank=True)
    details = models.TextField("Details", blank=True)

    def __str__(self):
        return self.created.strftime("%c"), self.subject
