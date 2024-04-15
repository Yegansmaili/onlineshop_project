from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class ActiveDisplayManager(models.Manager):

    def get_queryset(self):
        return super(ActiveDisplayManager, self).get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    objects = models.Manager()
    active_display_manager = ActiveDisplayManager()
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

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(BaseModel):
    PRODUCT_STARS = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Very Good'),
    )
    commented_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pro_comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_comments',
                             verbose_name='comment author')
    text = models.TextField(verbose_name='comment text')
    stars = models.CharField(choices=PRODUCT_STARS, max_length=2, verbose_name='What is your score?')

    def __str__(self):
        return self.user.username

    def get_stars_display(self):
        return dict(self.PRODUCT_STARS).get(self.stars, 'Unknown')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.commented_product.id])
