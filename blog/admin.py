from django.contrib import admin
from . models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'title',
        'intro',
        'date',
        'image',
    )



admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
