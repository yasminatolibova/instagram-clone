from django.contrib import admin

# Register your models here.
from .models import Story, Like
admin.site.register(Story)
admin.site.register(Like)
# admin.site.register(Comment)