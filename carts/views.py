from django.views.generic import ListView


class CartView(ListView):
    template_name = "cart.html"
    context_object_name = "items"

    def get_queryset(self):
        return []  # TODO return all items in the user's cart
