from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from orders.models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'address', 'order_created', 'is_paid', ]
    inlines = [OrderItemInline, ]


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]
