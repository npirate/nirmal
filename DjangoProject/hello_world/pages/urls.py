from django.urls import path

from .views import homePageView

urlpatterns = [
    path('',homePageView,name = 'home')#naming this url as home. must run the function homePageView which is already imported from .views
]