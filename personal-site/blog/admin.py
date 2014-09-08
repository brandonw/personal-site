from django.contrib import admin
from blog.models import Post, PostImage

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fields = ('name', 'pub_date',
            ('is_published', 'tags'),
            'post_text')

class PostImageAdmin(admin.ModelAdmin):
    fields = ('post', 'name', 'image')

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
