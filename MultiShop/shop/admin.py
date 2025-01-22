from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import *

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'get_image')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ("name",)}

    def get_image(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="50" height="50" />', obj.image.url)
        return '-'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'get_color', 'get_image')
    list_display_links = ('name',)
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {'slug': ("name",)}


    def get_color(self, product):
        colors = product.colors.all()
        if colors:
            return colors[0]
        return ''

    def get_image(self, product):
        images = product.images.all()
        if images:
            return mark_safe(f'<img src="{images[0].image.url}" width="100">')
        return ''

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)
    list_filter = ('product',)


admin.site.register(Color)
admin.site.register(Size)
# admin.site.register(ProductImage)


