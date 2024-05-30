from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class Cart:
    def __init__(self, request) -> None:
        """
        initializing the cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart
        super().__init__()

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        adding a new product to the cart
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        messages.success(self.request, _('your product has successfully been added'))

        self.save()

    def remove(self, product):
        """
        removing a product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('your product has been successfully removed'))
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['quantity'] * item['product_obj'].price
            yield item

    def __len__(self):
        """
        getting the length of the cart (how many products are in there)?
        """
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        removing the cart from the session
        """
        del self.session['cart']
        # messages.success(self.request, _('your cart has been successfully removed'))

        self.save()

    def get_total_price(self):
        # product_ids = self.cart.keys()
        # products = Product.objects.filter(id__in=product_ids)

        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())
        # total_price = 0
        #
        # for item in self.cart.keys():
        #     total_price += item['quantity'] * item['product_obj'].price
        #
        # return total_price

    def save(self):
        """
        saving the session when modified
        """
        self.session.modified = True
