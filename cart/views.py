import requests
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from cart.cart import Cart
from cart.forms import AddToCartProductForm
from products.models import Product
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['pro_update_quantity_form'] = AddToCartProductForm(
            initial={
                'quantity': item['quantity'],
                'inplace': True,
            }
        )

    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']

        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])
    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@require_POST
def clear_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
    else:
        messages.warning(request, _('your cart is already empty'))
    return redirect('product_list')
