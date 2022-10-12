from products.models import Product

from .testcases import SplinterTestCase


class ProductDetailPageTest(SplinterTestCase):

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
        self.browser.visit(f"{self.live_server_url}/products/{duck.id}/")
        self.assertEqual(self.browser.status_code, 200)
        assert self.browser.is_text_present(duck.name)
        assert self.browser.is_text_present(duck.description)
        assert self.browser.is_text_present(f"{duck.price}")
        assert self.browser.is_text_not_present(mouse.name)
        assert self.browser.is_text_not_present(mouse.description)
        assert self.browser.is_text_not_present(f"{mouse.price}")

    def test_missing_product(self):
        duck = Product.objects.create(
            name="duck",
            description="Adorable rubber duck",
            price=1.25,
        )
        self.browser.visit(f"{self.live_server_url}/products/{duck.id+1}/")
        self.assertEqual(self.browser.status_code, 404)
