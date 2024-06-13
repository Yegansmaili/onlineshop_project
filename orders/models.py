from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)  # phone_number field
    address = models.CharField(max_length=700)
    order_note = models.CharField(max_length=1000, blank=True, null=True,
                                  help_text=_('If you have a note, write  here. Otherwise, leave it blank. '))
    zarinpal_authority = models.CharField(max_length=256, blank=True, null=True, )

    order_created = models.DateTimeField(default=timezone.now)
    order_modified = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())

    def __str__(self):
        return f'Order {self.id} : {self.first_name} {self.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'order item {self.id} : {self.product}'
