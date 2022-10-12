from django.urls import path

from .views import product_details

urlpatterns = [
    path('products/<int:product_id>/', product_details),
]
