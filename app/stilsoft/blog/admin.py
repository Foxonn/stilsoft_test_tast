from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
