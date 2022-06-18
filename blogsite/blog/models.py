from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    content = RichTextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.body
class Sogi(models.Model):
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.bio