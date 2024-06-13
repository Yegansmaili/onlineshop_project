import json

import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = '#'
    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    request_data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,  # edit
        'amount': rial_total_price,
        'description': f'#{order_id}:{order.user.last_name}',
        'callback_url': '#',  # edit

    }
    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)

    data = res.json()['data']
    order.zarinpal_authority = data['authority']
    order.save()
    if 'errors' not in data or len(data['errors']) == 0:
        return redirect('zarinpal_pardakht')  # edit
    else:
        return HttpResponse('Errors from Zarinpal')
