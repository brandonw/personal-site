from django.contrib import admin
from blog.models import Post, PostTag, PostImage

class PostAdmin(admin.ModelAdmin):
    pass

class PostTagAdmin(admin.ModelAdmin):
    pass

class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(PostTag, PostTagAdmin)
admin.site.register(PostImage, PostImageAdmin)
