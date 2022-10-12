from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from splinter import Browser


class SplinterTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()
        self.browser = Browser("django")

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def visit(self, url_name):
        self.browser.visit(f"{self.live_server_url}{reverse(url_name)}")
