from django.db import models

def project_filename(project, original_name):
    return str(project.id)

class Project(models.Model):

    # affects ordering of the projects
    priority = models.PositiveSmallIntegerField()

    # a clear name to identify what a project is
    name = models.CharField(max_length=50)

    # a single image used to give a preview of what the project looks like
    thumbnail = models.ImageField(upload_to=project_filename)

    # a link to the repositor, if open sourced
    link = models.URLField(blank=True)

    # a brief description of what the project is
    short_descr = models.TextField()

    # an in-depth description of what the project is
    full_descr = models.TextField()

