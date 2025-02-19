from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
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


class OrderACall(models.Model):
    subscriber_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    subscriber_phone = models.CharField(max_length=20, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_call', null=False, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Заказ №{self.id}. {self.status.status_name}, {self.subscriber_name}"

    class Meta:
        verbose_name = 'Заказ звонка'
        verbose_name_plural = 'Заказ звонков'


class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       default=0)
    customer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='customer', null=True,
                                 default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=13, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=13, blank=True, null=True, default=None)
    comments = models.TextField(max_length=240, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status', null=False, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Заказ №{self.id}. {self.status.status_name}, {self.customer_name}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_in_oder', null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_in_oder', null=True,
                                default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в зазказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.discount_price
        self.price_per_item = price_per_item
        self.total_price = float(self.nmb) * float(price_per_item)

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_amount = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='basket', null=True,
                               default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_in_basket', null=True,
                              default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_in_basket', null=True,
                                default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в Корзине'
        verbose_name_plural = 'Товары в Корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.product.discount_price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)
