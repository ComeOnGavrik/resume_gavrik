from . import views
from django.urls import path, include


urlpatterns = [
    path('basket_adding', views.basket_adding, name='basket_adding'),
    path('checkout', views.checkout, name='checkout'),
    path('call_order', views.ordering_call, name='call_order'),
]
