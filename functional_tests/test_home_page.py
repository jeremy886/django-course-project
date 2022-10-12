from .testcases import SplinterTestCase


class HomePageTest(SplinterTestCase):

    def test_correct_status_and_page_content(self):
        self.browser.visit(self.live_server_url)
        self.assertEqual(self.browser.status_code, 200)
        assert self.browser.is_text_present('Welcome to my store')
