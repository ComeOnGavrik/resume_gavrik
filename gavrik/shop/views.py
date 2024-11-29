from django.shortcuts import render
from products.models import ProductImage


# Create your views here.
def shop_home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_phone = product_images.filter(product__category__id=1)
    product_images_laptop = product_images.filter(product__category__id=2)
    return render(request, 'shop/shop_home.html', locals())



