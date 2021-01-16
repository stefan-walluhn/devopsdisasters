from django.test import TestCase


class DevopsDisastersFixture(TestCase):
    fixtures = ['test.json']


class TestWebsite(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
