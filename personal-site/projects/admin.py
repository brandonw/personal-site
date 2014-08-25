from django.contrib import admin
from projects.models import Project, ProjectImage
from sorl.thumbnail.admin import AdminImageMixin

class ProjectAdmin(admin.ModelAdmin):
    pass

class ProjectImageAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
