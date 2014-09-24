from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from blog.models import Post
from taggit.models import Tag

class BlogHomeView(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        posts = Post.objects.order_by('-pub_date')
        if self.request.user.is_superuser:
            return posts
        else:
            return posts.filter(is_published=True)

class BlogPostView(DetailView):
    context_object_name = 'post'
    template_name = 'blog/post.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(is_published=True)

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

class BlogRssFeed(Feed):
    title = "Brandon Waskiewicz's blog"
    link = '/blog/'
    description = 'Inside my head'

    def items(self):
        return Post.objects.filter(is_published=True).order_by('-pub_date')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.get_preview()

class BlogAtomFeed(BlogRssFeed):
    feed_type = Atom1Feed
    subtitle = BlogRssFeed.title
