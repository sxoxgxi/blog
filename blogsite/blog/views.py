from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Post, Comment, Topic
from .profile_comps import get_quote
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    topics = Topic.objects.all()
    context = {'posts': posts, 'topics': topics}
    return render(request, 'blog/main.html', context)


def post(request, pk):
    try:
        previous_post = Post.objects.get(id=int(pk)-1)
    except Post.DoesNotExist:
        previous_post = "Dosen't exist"
    try:
        next_post = Post.objects.get(id=int(pk)+1) or "Dosen't exist"
    except Post.DoesNotExist:
        next_post = "Dosen't exist"
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
    context = {'post': post, 'comments': comments,
               'number': number, 'previous_post': previous_post, 'next_post': next_post}
    return render(request, 'blog/article.html', context)
    # return render(request, 'blog/misc.html', context)


def category(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'blog/categories.html', context)


def profile(request):
    quote = get_quote()[0]
    author = get_quote()[1]
    context = {'quote': quote, 'author': author}
    return HttpResponse("hello world")
    # return render(request, 'blog/profile.html', context)
