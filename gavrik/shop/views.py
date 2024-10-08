from django.shortcuts import render
from products.models import ProductImage


# Create your views here.
def shop_home(request):
    product = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'shop/shop_home.html', locals())
