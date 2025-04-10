from django.test import TestCase


class LoginTest(TestCase):
    def test_login_page_loads(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)