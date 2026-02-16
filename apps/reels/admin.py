from django.contrib import admin

# Register your models here.
from .models import Reel, Like
admin.site.register(Reel)
admin.site.register(Like)
# admin.site.register(Comment)