from django.shortcuts import render
from django.views import generic

from products.models import Product


class HomePageView(generic.TemplateView):

    def get_context_data(self, **kwargs):
        kwargs['products'] = Product.objects.filter(is_active=True).order_by('-created_at')[:5]
        return super().get_context_data(**kwargs)

    template_name = 'products/product_list.html'


class AboutUsView(generic.TemplateView):
    template_name = 'pages/about.html'
