from django.contrib import admin

from .models import Event, Location

# Register your models here.
admin.site.register(Location)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    date_hierarchy = "dayTime"
    list_display = ("name", "dayTime", "location")
    search_fields = ["name"]
