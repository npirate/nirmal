from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

# Create your views here.
class BlogListView (ListView):
    model = Post #where to pick the content from
    template_name = 'home.html' #where to show the content

class BlogDetailView (DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView (CreateView):#createview class will create a form with fields based on columns defined in Post model
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView (UpdateView):
    model = Post
    template_name ='post_edit.html'
    fields = ['title','body']