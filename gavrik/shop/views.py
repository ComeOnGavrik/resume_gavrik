from django.shortcuts import render
from products.models import ProductImage, Product
from .forms import SearchForm
from django.db.models import Q


# Create your views here.
def shop_home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_phone = product_images.filter(product__category__id=1)
    product_images_laptop = product_images.filter(product__category__id=2)
    return render(request, 'shop/shop_home.html', locals())


def search(request):
    form = SearchForm()
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            print(query, "!!!!!!!!")

            results = ProductImage.objects.filter(
                Q(product__name__icontains=query) | Q(product__description__icontains=query),
                is_active=True,
                is_main=True,
                product__is_active=True
            )
        else:
            query = "empty"
            results = []
    return render(request, 'shop/search.html', {'form': form, 'results': results,
                                                'search_line': query})


def showing_category_products(request, cat_name):
    cat_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True,
                                               product__category__name=cat_name)
    return render(request, 'shop/categories.html', {'cat_prods': cat_products})
