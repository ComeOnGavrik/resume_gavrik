from .models import ProductCategory


def dropping_down_category(request):
    product_categories = ProductCategory.objects.filter(is_active=True)
    print(product_categories)
    return locals()
