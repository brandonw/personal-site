# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

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
        r'^tags/(?P<slug>[\w-]+)/$',
        views.BlogTagView.as_view(),
        name='blog-tag'
    ),
)

