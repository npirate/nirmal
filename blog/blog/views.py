from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BlogDeleteView (DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home') #reverse lazy will not take user to home url pattern unless model deletes the the entry.
