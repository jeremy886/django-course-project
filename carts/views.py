from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from carts.models import Cart
from products.models import Product


class CartView(LoginRequiredMixin, ListView):
    template_name = "cart.html"
    context_object_name = "items"

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart.items.all()


class AddToCartView(LoginRequiredMixin, DetailView):
    http_method_names = ["post"]
    model = Product
    pk_url_kwarg = "product_id"

    def post(self, request, product_id):
        product = self.get_object()
        cart, created = Cart.objects.get_or_create(user=request.user)
        # TODO Add product to cart OR update product quantity (if it's already in the cart)
        # TODO show success message
        # TODO redirect to user's shopping cart page
