# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from projects import views

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(template_name='projects/home.html'),
        name='projects'),

    url(r'^(?P<id>\d+)/$',
        DetailView.as_view(template_name='projects/detail.html'),
        name='project-detail'),
    ),
)


