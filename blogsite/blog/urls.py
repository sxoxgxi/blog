from django.urls import path

from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<str:pk>', views.post, name='post'),
    path('categories/', views.category, name='cat'),
    path('sxoxgxi/', views.profile, name='profile'),
    
]
