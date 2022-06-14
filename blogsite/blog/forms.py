from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import User, Post, Comment


class BlogUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class Blog(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class BlogComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
