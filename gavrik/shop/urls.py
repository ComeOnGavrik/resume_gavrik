from . import views
from django.urls import path, include

urlpatterns = [
    path('home', views.shop_home, name='shop_home')
]