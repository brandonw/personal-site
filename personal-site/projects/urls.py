# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from projects import views

urlpatterns = patterns('',
    url(
        r'^$',
        TemplateView.as_view(template_name='projects/home.html'),
        name='projects'
    ),
)


