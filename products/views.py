from django.shortcuts import render

from .models import Product


def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_details.html', {
        'product': product,
    })
