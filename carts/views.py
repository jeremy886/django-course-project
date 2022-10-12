from django.views.generic import ListView

from carts.models import Cart


class CartView(ListView):
    template_name = "cart.html"
    context_object_name = "items"

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart.items.all()
