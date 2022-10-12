from django.test import TestCase

from products.models import Product


class ProductDetailPageTest(TestCase):

    def test_correct_product_shown(self):
        duck = Product.objects.create(
            name="duck",
            description="Adorable rubber duck",
            price=1.25,
        )
        mouse = Product.objects.create(
            name="mouse",
            description="A computer mouse",
            price=8.50,
        )
        response = self.client.get(f'/products/{duck.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, duck.name)
        self.assertContains(response, duck.description)
        self.assertContains(response, duck.price)
        self.assertNotContains(response, mouse.name)
        self.assertNotContains(response, mouse.description)
        self.assertNotContains(response, mouse.price)
