import requests
from django.shortcuts import render, redirect

from cart.cart import Cart
from cart.forms import AddToCartProductForm
from products.models import Product
from django.shortcuts import get_object_or_404


def cart_detail(request):
    cart = Cart(request)

    return render(request, 'cart/cart_detail.html', {'cart': cart})


def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)
    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')