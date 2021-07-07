from django.contrib import admin
from . models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = (
        'title',
        'intro',
        'date',
        'image',
    )

    list_filter = ('date',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date')
    list_filter = ('date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
