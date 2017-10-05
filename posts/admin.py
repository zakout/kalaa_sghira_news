from django.contrib import admin
from django.shortcuts import get_object_or_404

# Register your models here.

from .models import Post, Image


admin.site.register(Post)
admin.site.register(Image)