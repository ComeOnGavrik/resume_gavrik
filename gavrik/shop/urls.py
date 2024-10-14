from . import views
from django.urls import path, include
from products.views import ProductDetailView

urlpatterns = [
    path('home', views.shop_home, name='shop_home'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]