from django.test import TestCase

from .models import User


class UserModelTest(TestCase):

    """Unit tests for Custom User model."""

    def test_user_creation(self):
        """Create a valid user and save it."""
        email = 'test@email.com'
        password = '12345'
        user = User.objects.create(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.get_short_name(), email)
        self.assertEqual(user.get_full_name(), email)
