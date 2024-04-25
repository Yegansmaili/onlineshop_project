from django.shortcuts import render
from django.views import generic


class CartDetailView(generic.TemplateView):
    template_name = 'cart/cart_detail.html'
