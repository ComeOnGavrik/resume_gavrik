from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Product
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from products.models import ProductImage


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.product_image.all()
        context['cards'] = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)[:5]
        return context

    def get(self, request, *args, **kwargs):
        # Создание session_key, если он еще не существует
        if not request.session.session_key:
            request.session.create()
            # Устанавливаем session_key в сессии
        request.session['session_key'] = request.session.session_key
        return super().get(request, *args, **kwargs)

