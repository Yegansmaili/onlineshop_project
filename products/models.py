from django.db import models
from django.urls import reverse

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Product(BaseModel):
    STATUS_CHOICES = (
        ('available', 'available'),
        ('unavailable', 'Out of stock'),
        ('new', 'new'),
        ('preparing', 'preparing'),
        ('charged', 'charged'),
        ('Limited', 'Limited')

    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='available', null=True, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('')


