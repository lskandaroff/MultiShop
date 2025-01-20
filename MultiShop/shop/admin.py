from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ("name",)}

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
        print(colors)
        if colors:
            return colors[0]
        return ''

    def get_image(self, product):
        images = product.productimage_set.all()
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


