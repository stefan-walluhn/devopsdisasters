from django.test import TestCase

from devopsdisasters.categories.models import Category


class TestFailedCategory(TestCase):
    def setUp(self):
        self.category = Category(name="category name",
                                 intro="<p>category intro</p>")

    def test_category(self):
        self.assertIsInstance(self.category, Category)

    def test_to_str(self):
        self.assertEqual(str(self.category), 'category name')

    def test_name(self):
        self.assertEqual(self.category.name, 'category name')

    def test_intro(self):
        self.assertEqual(self.category.intro, '<p>category intro</p>')

    def test_slug(self):
        self.category.save()
        self.category.refresh_from_db()
        self.assertEqual(self.category.slug, 'category-name')
