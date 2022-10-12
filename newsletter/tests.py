from django.test import TestCase

from .models import Subscriber


class SubscriberModelTests(TestCase):

    """Tests for Subscriber model."""

    def test_creation(self):
        """Create a save a valid Subscriber."""
        name = "Mae Mahoney"
        email = "mae@mahoney.name"
        subscriber = Subscriber(name=name, email=email)
        subscriber.save()
        self.assertEqual(subscriber.name, name)
        self.assertEqual(subscriber.email, email)
