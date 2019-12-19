from django.core.exceptions import ValidationError

from wagtail.tests.utils import WagtailPageTests

from home.models import HomePage
from failed.models import FailedIndexPage, FailedPage


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

    def test_fail(self):
        page = FailedPage(fail="<p>failed fail</p>")
        self.assertEqual(page.fail, '<p>failed fail</p>')

    def test_fail_cannot_be_blank(self):
        page = FailedPage()
        with self.assertRaises(ValidationError) as ve:
            page.full_clean()

        self.assertIn('fail', ve.exception.error_dict)

    def test_lessons_learned(self):
        page = FailedPage(lessons_learned="<p>failed lessons learned</p>")
        self.assertEqual(page.lessons_learned, '<p>failed lessons learned</p>')

    def test_lessons_learned_cannot_be_blank(self):
        page = FailedPage()
        with self.assertRaises(ValidationError) as ve:
            page.full_clean()

        self.assertIn('lessons_learned', ve.exception.error_dict)
