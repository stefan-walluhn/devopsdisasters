from django.test import TestCase


class DevopsDisastersFixture(TestCase):
    fixtures = ['test.json']


class TestWebsite(DevopsDisastersFixture, TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_failed(self):
        response = self.client.get('/failed/')
        self.assertEqual(response.status_code, 200)

    def test_failed_by_category(self):
        response = self.client.get('/failed/category/foo_category/')
        self.assertEqual(response.status_code, 200)

    def test_failed_by_unknown_category(self):
        response = self.client.get('/failed/category/unknown_category/')
        self.assertEqual(response.status_code, 404)

    def test_failed_by_empty_category(self):
        response = self.client.get('/failed/category/')
        self.assertEqual(response.status_code, 404)
