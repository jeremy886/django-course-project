from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from splinter import Browser


class SplinterTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()
        self.browser = Browser("django")

    def tearDown(self):
        self.browser.quit()
        super().tearDown()
