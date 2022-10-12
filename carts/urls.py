from django.urls import path
from .views import CartView, AddToCartView, CartItemView


app_name = 'carts'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add'),
    path('cart/items/<int:pk>/', CartItemView.as_view(), name='item'),
]
