from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404

from blog.models import Post
from misc.code_blocks_preprocessor import CodeBlockExtension

from taggit.models import Tag
import markdown

class BlogHomeView(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects
        else:
            return Post.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['published_tags'] = Post.objects.filter(is_published=True)
        return context

class BlogPostView(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        context['html'] = markdown.markdown(
                context['object'].post_text,
                extensions=[CodeBlockExtension()])
        return context

class BlogTagView(TemplateView):
    template_name = 'blog/tag.html'

    def get_context_data(self, **kwargs):
        context = super(BlogTagView, self).get_context_data(**kwargs)
        tagslug =  self.kwargs['slug']
        tag = Tag.objects.get(slug=tagslug)
        context['tag'] = tag.name
        context['taggedposts'] = (Post.objects
            .filter(is_published=True)
            .filter(tags__name=tag.name)
            .distinct())

        context['published_tags'] = Post.objects.filter(is_published=True)
        return context
