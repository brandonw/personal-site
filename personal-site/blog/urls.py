# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from blog import views

urlpatterns = patterns('',
    url(
        r'^$',
        views.BlogHomeView.as_view(),
        name='blog'
    ),
    url(
        r'^posts/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$',
        views.BlogPostView.as_view(),
        name='blog-post'
    ),
    url(
        r'^tags/(?P<tag>[\w-]+)/$',
        views.BlogTagView.as_view(),
        name='blog-tag'
    ),
)

