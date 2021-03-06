from django.test import TestCase


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_wrong_url_returns_404(self):
        response = self.client.get('/wrong_url/')
        self.assertTemplateUsed(response, '../templates/404.html')
