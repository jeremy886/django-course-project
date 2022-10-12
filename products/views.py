from django.shortcuts import render
from django.views.generic import DetailView

from .models import Product


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_id'
    template_name = 'product_details.html'


def product_list(request):
    return render(request, 'product_list.html', {
        'products': Product.objects.all(),
    })
