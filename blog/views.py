from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# A class based view
class view_blog(ListView):
    model = Post
    template_name = 'blog.html'


class view_article_details(DetailView):
    model = Post
    template_name = 'article_details.html'
