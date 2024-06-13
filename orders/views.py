from django.shortcuts import render, redirect
from .models import *
from cart.cart import Cart
from .forms import OrderForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, _('your cart is empty. Go shopping!'))
        return redirect('product_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    product=product,
                    order=order_obj,
                    price=product.price,
                    quantity=item['quantity']
                )
            # cart.clear()
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
            # messages.success(request, _('your order has been created'))
            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')

    return render(request, 'orders/order_create.html', context={
        'form': order_form
    })
