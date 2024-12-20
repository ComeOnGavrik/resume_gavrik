# views.py
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import ProductInBasket, Order, Status, ProductInOrder, OrderACall
from products.models import ProductImage
from .forms import CheckoutContactsForm, OrderACallForm


def basket_adding(request):
    print('Вызвался баскет адинг2')
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    print("_________________________")
    print(data)
    print("_________________________")
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
                                                                         is_active=True, defaults={"nmb": nmb})
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


def checkout(request):
    # product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    print(request.user)
    form = CheckoutContactsForm(request.POST or None)
    if not request.user.is_authenticated:
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()

        products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    else:
        products_in_basket = ProductInBasket.objects.filter(author=request.user, is_active=True)

    products_in_basket_ph_ids = []
    for el in products_in_basket:
        products_in_basket_ph_ids.append(el.product.id)

    products_in_basket_ph = ProductImage.objects.filter(is_active=True, product__is_active=True, is_main=True,
                                                        product__id__in=products_in_basket_ph_ids)

    if request.POST:
        print('______________________TEST')
        print(request.POST)
        data = request.POST
        print("data:")
        print(data)
        if form.is_valid():
            print("yes")
            order = Order.objects.create(customer=request.user, customer_name=form.cleaned_data["user_name"],
                                         customer_phone=form.cleaned_data["user_phone"],
                                         customer_address=form.cleaned_data["user_address"],
                                         comments=form.cleaned_data["user_comment"], status=Status.objects.all()[0])

            for name, value in data.items():
                if name.startswith("product_in_basket_el_"):
                    id_el = name.split("product_in_basket_el_")
                    print(id_el[1], '---', value)
                    prod = ProductInBasket.objects.get(id=id_el[1])
                    prod.nmb = value
                    prod.save(force_update=True)
                    product_in_order = ProductInOrder.objects.create(order=order, product=prod.product, nmb=value)

            return redirect('shop_home')
        else:
            print("mistake")
    return render(request, 'shop/checkout.html', locals())


def ordering_call(request):
    form = OrderACallForm(request.POST or None)
    if form.is_valid():
        OrderACall.objects.create(subscriber_name=form.cleaned_data["subscriber_name"],
                                  subscriber_phone=form.cleaned_data["subscriber_phone"],
                                  status=Status.objects.all()[0])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
