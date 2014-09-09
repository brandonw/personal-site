from django.shortcuts import render
from django.views.generic.detail import DetailView

from projects.models import Project
from misc.code_blocks_preprocessor import CodeBlockExtension

import markdown

class ProjectDetailView(DetailView):
    model = Project
    context_object_name='project'
    template_name = 'projects/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('priority')
        context['html'] = markdown.markdown(
                context['object'].full_descr,
                extensions=[CodeBlockExtension()])
        return context

