from django.urls import path

from .views import ProductDetailView, product_list

urlpatterns = [
    path('products/<int:product_id>/', ProductDetailView.as_view()),
    path('products/', product_list),
]
