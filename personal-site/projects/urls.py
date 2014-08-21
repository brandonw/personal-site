# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from projects import views
from projects.models import Project

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(template_name='projects/home.html',
                         model=Project,
                         context_object_name='projects',
                         queryset=Project.objects.order_by('priority')),
        name='projects'),

    url(r'^(?P<slug>[\w-]+)/$',
        DetailView.as_view(template_name='projects/detail.html',
                           model=Project,
                           context_object_name='project'),
        name='project-detail'),
)


