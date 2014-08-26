from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from blog.models import Post

class BlogHomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.order_by('-pub_date', '-pub_time').first()
        context['posts'] = Post.objects.order_by('-pub_date', '-pub_time')
        return context

class BlogPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-pub_date', '-pub_time')
        return context
