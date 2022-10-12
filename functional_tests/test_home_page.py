from django.test import TestCase


class HomePageTest(TestCase):

    def test_correct_status_and_page_content(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to my store')
