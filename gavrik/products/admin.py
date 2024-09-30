from django.contrib import admin

from products.models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['id', 'name', 'description', 'is_active']
    search_fields = ['name']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['product', 'image', 'is_active']
    search_fields = ['product']

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
