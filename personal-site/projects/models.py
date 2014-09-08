from django.db import models
from os.path import splitext
from autoslug import AutoSlugField
from markupfield.fields import MarkupField
from sorl.thumbnail import ImageField

def get_slug(project_image, original_name):
    extension = splitext(original_name)
    return str(project_image.project.slug) + extension[1]

class Project(models.Model):

    # affects ordering of the projects
    priority = models.PositiveSmallIntegerField(unique=True,
        help_text='Projects will be ordered by this value.')

    # a clear name to identify what a project is
    name = models.CharField(max_length=50,
        help_text='The name of the project.')

    # unique slug, based off of name
    slug = AutoSlugField(populate_from='name', unique=True)

    # a link to the repository, if open sourced
    link = models.URLField(blank=True,
        help_text='An optional URL to the project.')

    # a brief description of what the project is, in plain text format
    short_descr = models.TextField(
        help_text='A short description displayed in the project index. ' +
        'This will be html escaped, so ensure it is plain text.')

    # an in-depth description of what the project is, in Markdown format
    full_descr = MarkupField(markup_type='markdown',
        help_text='The full description of the project, in Markdown format. ' +
        'The value of this field  will not be html escaped.')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project-detail', args=[str(self.slug)])

class ProjectImage(models.Model):

    project = models.ForeignKey(Project,
        help_text='The project this image is related to.')

    image = ImageField(upload_to=get_slug,
        help_text='An image that should showcase what the project is or does.')

    def __unicode__(self):
        return self.project.name

    def get_absolute_url(self):
        return self.image.url
