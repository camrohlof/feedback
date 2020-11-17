from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.


class Location(models.Model):
    party_area = models.CharField(max_length=20)

    def __str__(self):
        return self.party_area


class Event(TimeStampedModel):
    name = models.CharField("Name of Event", max_length=50)
    dayTime = models.DateTimeField()
    timeBefore = models.IntegerField(default=2)
    timeAfter = models.IntegerField(default=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name + ": " + str(self.dayTime)
