from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.shop_home, name='shop_home')
]