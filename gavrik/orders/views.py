# views.py
from django.http import JsonResponse
from django.shortcuts import render

from .models import ProductInBasket


def basket_adding(request):
    print('Вызвался баскет адинг')
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete:
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:

        if request.user.is_authenticated:
            new_product, created = ProductInBasket.objects.get_or_create(product_id=product_id, author=request.user,
                                                                         is_active=True, defaults={"nmb": nmb})
        else:
            new_product, created = ProductInBasket.objects.get_or_create(product_id=product_id, session_key=session_key,
                                                                         defaults={"nmb": nmb})
        if not created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)
    if request.user.is_authenticated:
        products_in_basket = ProductInBasket.objects.filter(author=request.user, is_active=True)
    else:
        products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    print(products_total_nmb)

    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)
