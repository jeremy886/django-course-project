from .testcases import SplinterTestCase


class NavbarTest(SplinterTestCase):

    def test_clicking_about_link(self):
        """Test About link URL and active state work correctly."""
        self.browser.visit(self.live_server_url)  # Visit homepage
        about_link = self.browser.find_by_text("About")
        assert not about_link.has_class("active")  # About link isn't active
        about_link.click()  # Click About link
        self.assertEqual(self.browser.url, "/about/")
        assert not about_link.has_class("active")  # About link is active
