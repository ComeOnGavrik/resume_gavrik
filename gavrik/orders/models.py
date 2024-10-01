from django.db import models

from products.models import Product


# Create your models here.

class Status(models.Model):
    status_name = models.CharField(max_length=15, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) #total price dor all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=13, blank=True, null=True, default='+375')
    customer_address = models.CharField(max_length=13, blank=True, null=True, default='+375')
    comments = models.TextField(max_length=240, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status', null=False, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Заказ №{self.id}. {self.status.status_name}, {self.customer_name}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_in_oder', null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_in_oder', null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
