from django.contrib import admin

from .models import Comment, Note

# Register your models here.
admin.site.register(Note)
admin.site.register(Comment)
