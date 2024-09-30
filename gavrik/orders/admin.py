from django.contrib import admin

from orders.models import Order, ProductInOrder, Status


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['customer_name', 'customer_email', 'customer_phone', 'comments', 'status']
    search_fields = ['customer_name']

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['order', 'product', 'is_active']
    search_fields = ['order']

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['status_name', 'is_active']
    search_fields = ['status_name']

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)
