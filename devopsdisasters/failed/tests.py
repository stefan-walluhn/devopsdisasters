from django.core.exceptions import ValidationError

from wagtail.core.rich_text import RichText
from wagtail.tests.utils import WagtailPageTests

from devopsdisasters.categories.models import Category
from devopsdisasters.home.models import HomePage
from devopsdisasters.failed.models import FailedIndexPage, FailedPage


class TestFailedIndexPage(WagtailPageTests):
    def test_can_create_under_home_page(self):
        self.assertCanCreateAt(HomePage, FailedIndexPage)

    def test_sub_page_types(self):
        self.assertAllowedSubpageTypes(FailedIndexPage, [FailedPage])

    def test_intro(self):
        page = FailedIndexPage(intro="<p>failed index intro</p>")
        self.assertEqual(page.intro, '<p>failed index intro</p>')

    def test_intro_cannot_be_blank(self):
        page = FailedIndexPage()
        with self.assertRaises(ValidationError) as ve:
            page.full_clean()

        self.assertIn('intro', ve.exception.error_dict)


class TestFailedPage(WagtailPageTests):
    def test_can_create_under_failed_index_page(self):
        self.assertCanCreateAt(FailedIndexPage, FailedPage)

    def test_parent_page_types(self):
        self.assertAllowedParentPageTypes(FailedPage, [FailedIndexPage])

    def test_sub_page_types(self):
        self.assertAllowedSubpageTypes(FailedPage, [])

    def test_quote(self):
        page = FailedPage(quote="failed quote")
        self.assertEqual(page.quote, 'failed quote')

    def test_quote_can_be_blank(self):
        page = FailedPage()
        try:
            page.clean_fields(
                exclude=['path', 'depth', 'title', 'slug', 'lessons_learned'])
        except Exception:
            self.fail('blank quote should not raise on validation')

    def test_fail(self):
        page = FailedPage(fail=[('paragraph', RichText('<p>failed fail</p>'))])
        self.assertEqual(
            page.fail.render_as_block(),
            '<div class="block-paragraph"><p>failed fail</p></div>')

    def test_lessons_learned(self):
        page = FailedPage(lessons_learned="<p>failed lessons learned</p>")
        self.assertEqual(page.lessons_learned, '<p>failed lessons learned</p>')

    def test_lessons_learned_cannot_be_blank(self):
        page = FailedPage()
        with self.assertRaises(ValidationError) as ve:
            page.clean_fields()

        self.assertIn('lessons_learned', ve.exception.error_dict)

    def test_category(self):
        category = Category(name="failed category name")
        page = FailedPage(categories=[category])
        self.assertListEqual(list(page.categories.all()), [category])
