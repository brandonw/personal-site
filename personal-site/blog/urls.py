# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from blog import views

urlpatterns = patterns('',
    url(
        r'^$',
        TemplateView.as_view(template_name='blog/blog_home.html'),
        name='blog'
    ),
)

