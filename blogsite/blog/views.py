from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import Blog, BlogUser, BlogComment
from .profile_comps import get_quote
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post(request, pk):
    form = BlogComment()
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()
    number = comments.count()
    if request.method == 'POST':
        comment = Comment.objects.create(
            post=post,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            body=request.POST.get('body')
        )
    context = {'post': post, 'comments': comments, 'form': form, 'number': number}
    print(comments)
    return render(request, 'blog/article.html', context)
    # return render(request, 'blog/misc.html', context)


def category(request):
    post = Post.objects.all()
    # topics = post.topic_set.all()
    context = {'post': post}
    return render(request, 'blog/categories.html', context)


def profile(request):
    quote = get_quote()[0]
    author = get_quote()[1]
    context = {'quote': quote, 'author': author}
    return HttpResponse("hello world")
    # return render(request, 'blog/profile.html', context)