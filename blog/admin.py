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

    list_filter = ('date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
