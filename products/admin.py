from django.contrib import admin
from .models import Category, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'on_sale',
        'image',
    )

    ordering = ('sku',)
    readonly_fields = ('sku',)
    list_filter = ('category__friendly_name', 'on_sale',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
