from django.test import TestCase

from users.models import User
from .models import Cart


class CartModelTest(TestCase):

    """Unit tests for Cart model."""

    def test_creation(self):
        user = User.objects.create(email="test@email.com", password="12345")
        cart = Cart.objects.create(user=user)
        self.assertEqual(cart.user, user)

    def test_string_representation(self):
        user = User.objects.create(email="test@email.com", password="12345")
        cart = Cart.objects.create(user=user)
        self.assertEqual(str(cart), "Cart for test@email.com")
