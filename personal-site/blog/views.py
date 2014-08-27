from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from blog.models import Post, PostTag

class BlogHomeView(TemplateView):
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.order_by('-pub_date', '-pub_time').first()
        context['posts'] = Post.objects.grouped_by_date()
        return context

class BlogPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.grouped_by_date()
        return context

class BlogTagView(TemplateView):
    template_name = 'blog/tag.html'

    def get_context_data(self, **kwargs):
        context = super(BlogTagView, self).get_context_data(**kwargs)
        context['tag'] =  kwargs['tag']
        context['posttags'] = PostTag.objects.filter(tag__iexact=context['tag'])
        context['posts'] = Post.objects.grouped_by_date()
        return context
