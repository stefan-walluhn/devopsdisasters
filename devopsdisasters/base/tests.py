from django.conf import settings
from django.test import TestCase


class DevopsDisastersFixture(TestCase):
    fixtures = ['test.json']


class TestWebsite(DevopsDisastersFixture, TestCase):
    category_route = settings.DEVOPSDISASTERS_CATEGORY_ROUTE

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_failed(self):
        response = self.client.get('/failed/')
        self.assertEqual(response.status_code, 200)

    def test_failed_by_category(self):
        response = self.client.get(
            '/failed/{}/foo_category/'.format(self.category_route)
        )
        self.assertEqual(response.status_code, 200)

    def test_failed_by_unknown_category(self):
        response = self.client.get(
            '/failed/{}/unknown_category/'.format(self.category_route)
        )
        self.assertEqual(response.status_code, 404)

    def test_failed_by_empty_category(self):
        response = self.client.get('/failed/{}/'.format(self.category_route))
        self.assertEqual(response.status_code, 404)
