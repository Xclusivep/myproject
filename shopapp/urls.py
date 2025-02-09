from django.urls import path
from  . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("blog01/", views.blog01, name= "blog01"),
    path("home02/", views.home02, name="home02"),
    path("home03/", views.home03, name="home03"),
    path("home04/", views.home04, name="home04"),
    path("home05/", views.home05, name="home05"),
    path("blog_grid/", views.blog_grid, name="blog_grid"),
    path("blog_list_left/", views.blog_list2, name="blog_list2"),
    path("blogs/", views.blog_list, name="blog_list"),


]