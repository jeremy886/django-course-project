from django.test import TestCase

from products.models import Product


class ProductListPageTest(TestCase):

    def test_all_products_shown(self):
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
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, duck.name)
        self.assertContains(response, duck.description)
        self.assertContains(response, duck.price)
        self.assertContains(response, mouse.name)
        self.assertContains(response, mouse.description)
        self.assertContains(response, mouse.price)
