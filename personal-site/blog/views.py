from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from taggit.models import Tag

from blog.models import Post

class BlogHomeView(TemplateView):
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        post_qty = Post.objects.count()
        if post_qty > 0:
            context['post'] = Post.objects.order_by('-pub_date', '-pub_time')[0]
        if post_qty > 1:
            context['prev'] = Post.objects.order_by('-pub_date', '-pub_time')[1]
        context['posts'] = Post.objects.group_by_date()
        return context

def get_wrapped_posts(groups, slug):
    prev = None
    next = None
    hit = False
    for group in groups:
        for post in group.posts:
            if hit == False and post.slug != slug:
                next = post
            if hit == True:
                prev = post
                return (prev, next)
            if post.slug == slug:
                hit = True
    return (prev, next)

class BlogPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        groups = Post.objects.group_by_date()
        context['posts'] = groups

        (prev, next) = get_wrapped_posts(groups, self.kwargs['slug'])
        context['prev'] = prev
        context['next'] = next
        return context

class BlogTagView(TemplateView):
    template_name = 'blog/tag.html'

    def get_context_data(self, **kwargs):
        context = super(BlogTagView, self).get_context_data(**kwargs)
        tagslug =  self.kwargs['slug']
        tag = Tag.objects.get(slug=tagslug)
        context['tag'] = tag.name
        context['taggedposts'] = Post.objects.filter(tags__name__exact=tag.name).distinct()
        context['posts'] = Post.objects.group_by_date()
        return context
