from . import views
from django.urls import path, include
from products.views import ProductDetailView

urlpatterns = [
    path('home', views.shop_home, name='shop_home'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('', include('orders.urls')),
    path('search/', views.search, name='search'),
    path('category/<str:cat_name>', views.showing_category_products, name='category_products'),
]
