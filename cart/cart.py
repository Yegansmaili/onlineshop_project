from products.models import Product


class Cart:
    def __init__(self, request) -> None:
        """
        initializing the cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get['cart']
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart
        super().__init__()

    def add(self, product, quantity=1):
        """
        adding a new product to the cart
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """
        removing a product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        """
        getting the length of the cart (how many products are in there)?
        """
        return len(self.cart.keys())

    def clear(self):
        """
        removing the cart from the session
        """
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum(product.price for product in products)

    def save(self):
        """
        saving the session when modified
        """
        self.session.modified = True
