from django.test import TestCase


class NewsletterPageTest(TestCase):

    def test_correct_status_and_page_content(self):
        response = self.client.get('/newsletter/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign up for our newsletter')
