from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class ActiveDisplayManager(models.Manager):

    def get_queryset(self):
        return super(ActiveDisplayManager, self).get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    objects = models.Manager()
    active_display_manager = ActiveDisplayManager()
    created_at = models.DateTimeField(default=timezone.now,verbose_name=_('creation time'))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_('modified time'))
    is_active = models.BooleanField(default=True,verbose_name=_('activity status'))


class Product(BaseModel):
    STATUS_CHOICES = (
        ('available', _('available')),
        ('unavailable', _('Out of stock')),
        ('new', _('new')),
        ('preparing', _('preparing')),
        ('charged', _('charged')),
        ('Limited', _('Limited'))

    )
    title = models.CharField(max_length=100,verbose_name=_('title'))
    description = RichTextField(verbose_name=_('description'))
    short_description = RichTextField(max_length=300, blank=True, null=True,verbose_name=_('short description'))
    price = models.PositiveIntegerField(default=0,verbose_name=_('price'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='available', null=True, blank=True,
                              verbose_name=_('status'))
    cover = models.ImageField(upload_to='product/covers/', null=True, blank=True, verbose_name=_('cover'))

    def __str__(self):
        return self.title

    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, 'Unknown')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(BaseModel):
    PRODUCT_STARS = (
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Very Good')),
    )
    commented_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pro_comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_comments',
                             verbose_name=_('comment author'))

    text = models.TextField(verbose_name=_('comment text'))
    stars = models.CharField(choices=PRODUCT_STARS, max_length=2, verbose_name=_('What is your score?'))

    def __str__(self):
        return self.user.username

    def get_stars_display(self):
        return dict(self.PRODUCT_STARS).get(self.stars, 'Unknown')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.commented_product.id])
