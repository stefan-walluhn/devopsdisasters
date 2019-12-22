from django.test import TestCase

from categories.models import Category


class TestFailedCategory(TestCase):
    def setUp(self):
        self.category = Category(name="category name")

    def test_category(self):
        self.assertIsInstance(self.category, Category)

    def test_to_str(self):
        self.assertEqual(str(self.category), 'category name')

    def test_name(self):
        self.assertEqual(self.category.name, 'category name')
