from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    ColorModel,
    ProductCategoryModel,
    ProductTagModel,
    ProductSizeModel,
    ProductModel,
    ProductImageModel,
)

@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')
    search_fields = ('name', 'code')
    list_filter = ('code',)

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')
    search_fields = ('title',)
    list_filter = ('parent',)
    autocomplete_fields = ('parent',)

@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1
    verbose_name = _('Product Image')
    verbose_name_plural = _('Product Images')

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'sku')
    search_fields = ('title', 'sku', 'description')
    list_filter = ('categories', 'colors', 'tags', 'sizes')
    autocomplete_fields = ('colors', 'tags', 'categories', 'sizes')
    inlines = [ProductImageInline]

@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    search_fields = ('product__title',)
    autocomplete_fields = ('product',)
