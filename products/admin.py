from django.contrib import admin
from .models import *


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'text','is_active','stars', ]
    extra = 1
    fk_name = 'commented_product'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'updated_at']
    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'commented_product', 'is_active', 'created_at', ]
