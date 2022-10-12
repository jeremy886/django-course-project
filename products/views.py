from django.shortcuts import render, get_object_or_404

from .models import Product


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {
        'product': product,
    })


def product_list(request):
    return render(request, 'product_list.html', {
        'products': Product.objects.all(),
    })
