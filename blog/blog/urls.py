from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

#list of pairs of url-view along with name of this pair

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name = 'post_edit') 
]