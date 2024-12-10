from django.contrib import admin

from .models import Product, ProductImage, ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id', 'name', 'discount_price', 'price', 'is_active']
    search_fields = ['name']
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id', 'product', 'image', 'is_active']
    search_fields = ['product']

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
