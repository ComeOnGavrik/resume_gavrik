from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import ProductImage
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView


class ProductDetailView(DetailView):
    model = ProductImage
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
