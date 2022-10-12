from django.test import TestCase


class AboutPageTest(TestCase):

    def test_correct_status_and_page_content(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'We were founded in 2022')
