from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = 'addTime'
    template_name = 'all_news.html'
    context_object_name = 'all_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_time'] = Post.addTime
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
