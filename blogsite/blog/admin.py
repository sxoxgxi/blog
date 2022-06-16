from mimetypes import common_types
from django.contrib import admin

from .models import Post, Comment, Topic
# Register your models here.

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)
