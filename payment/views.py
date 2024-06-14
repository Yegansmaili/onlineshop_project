import json

import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

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
        'callback_url': request.build_absolute_uri(reverse('payment:payment_callback')),  # edit

    }
    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)

    data = res.json()['data']
    order.zarinpal_authority = data['authority']
    order.save()
    if 'errors' not in data or len(data['errors']) == 0:
        return redirect('zarinpal_pardakht')  # edit
    else:
        return HttpResponse('Errors from Zarinpal')


def payment_callback(request):
    payment_authority = request.GET.get('authority')
    payment_status = request.GET.get('status')
    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    if payment_status == 'OK':
        request_header = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }
        request_data = {
            'merchant_id': settings.ZARINPAL_MERCHANT_ID,  # edit
            'amount': rial_total_price,
            'authority': payment_authority,
        }
        res = requests.post(url='url.com/..',
                            data=json.dumps(request_data),
                            headers=request_header,
                            )
        if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res.json()['data']['errors']) == 0):

            data = res.json()['data']
            payment_code = data['code']

            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()
                return HttpResponse('پرداخت با موفقیت انجام شد')
            elif payment_code == 101:
                return HttpResponse('تراکنش شما قبلا ثبت شده است')
            else:
                error_code = res.json()['errors']['code']
                error_message = res.json()['errors']['message']
                return HttpResponse(f'تراکنش ناموفق{error_message}{error_code}')

    else:
        return HttpResponse('تراکنش انجام نشد')