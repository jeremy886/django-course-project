from .testcases import SplinterTestCase


class NavbarTest(SplinterTestCase):

    def test_clicking_about_link(self):
        """Test About link URL and active state work correctly."""
        self.visit("home")  # Visit homepage
        about_link = self.browser.find_by_text("About")
        assert not about_link.has_class("active")  # About link isn't active
        about_link.click()  # Click About link
        self.assertEqual(self.browser.url, self.reverse("about"))
        assert not about_link.has_class("active")  # About link is active

    def test_clicking_newsletter_link(self):
        """Test Newsletter link URL and active state work correctly."""
        self.visit("home")  # Visit homepage
        newsletter_link = self.browser.find_by_text("Newsletter")
        assert not newsletter_link.has_class("active")  # Link isn't active
        newsletter_link.click()  # Click link
        self.assertEqual(
            self.browser.url,
            self.reverse("newsletter:subscribe"),
        )
        assert not newsletter_link.has_class("active")  # Link is active
