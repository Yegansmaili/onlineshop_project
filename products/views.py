from django.shortcuts import render
from django.views import generic
from .models import *


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(is_active=True).order_by('-created_at')
    # queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
