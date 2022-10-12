from django.urls import path

from .views import product_details, product_list

urlpatterns = [
    path('products/<int:product_id>/', product_details),
    path('products/', product_list),
]
