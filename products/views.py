from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.translation import gettext_lazy as _

from cart.forms import AddToCartProductForm
from .forms import CommentForm
from .models import *


class ProductListView(generic.ListView):
    # queryset = Product.objects.filter(is_active=True).order_by('-created_at')
    queryset = Product.active_display_manager.all().order_by('-created_at')
    template_name = 'products/product_list.html'
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        # kwargs['comment_count'] = product.pro_comments.filter(is_active=True).count()   customized with template tags
        kwargs['comments'] = product.pro_comments.all().order_by('-created_at')
        kwargs['comment_form'] = CommentForm()
        # kwargs['AddToCartProductForm']= AddToCartProductForm()

        return super().get_context_data(**kwargs)


class CommentCreateView(generic.CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        neww = form.save(commit=False)
        neww.user = self.request.user
        pro_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=pro_id)
        neww.commented_product = product
        messages.success(self.request,_('your comment has been successfully sent'))
        return super().form_valid(form)

# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     # comment = product.pro_comments.filter(is_active=True)
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_c = comment_form.save(commit=False)
#             new_c.user = request.user
#             new_c.commented_product = product
#             new_c.save()
#
#     else:
#         comment_form = CommentForm()
#
#     return render(request, 'products/product_detail.html', context={
#         'product': product,
#         'comment_form': comment_form,
#     })

# def say_hello(request):
#     result = _('Hello')
#     return HttpResponse(result)
