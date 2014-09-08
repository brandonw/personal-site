from django.contrib import admin
from projects.models import Project, ProjectImage
from sorl.thumbnail.admin import AdminImageMixin

class ProjectAdmin(admin.ModelAdmin):
    fields = (('name', 'priority'),
        'link', 'short_descr', 'full_descr')

class ProjectImageAdmin(AdminImageMixin, admin.ModelAdmin):
    fields = ('project', 'image')

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
