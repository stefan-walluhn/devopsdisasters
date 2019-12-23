from wagtail.tests.utils import WagtailPageTests

from devopsdisasters.categories.models import Category
from devopsdisasters.home.models import HomePage
from devopsdisasters.howto.models import HowToIndexPage, HowToPage


class TestHowToIndexPage(WagtailPageTests):
    def test_can_create_under_home_page(self):
        self.assertCanCreateAt(HomePage, HowToIndexPage)

    def test_sub_page_types(self):
        self.assertAllowedSubpageTypes(HowToIndexPage, [HowToPage])


class TestHowToPage(WagtailPageTests):
    def test_can_create_under_how_to_index_page(self):
        self.assertCanCreateAt(HowToIndexPage, HowToPage)

    def test_parent_page_types(self):
        self.assertAllowedParentPageTypes(HowToPage, [HowToIndexPage])

    def test_category(self):
        category = Category(name="howto category name")
        page = HowToPage(categories=[category])
        self.assertListEqual(list(page.categories.all()), [category])

    def test_abstract(self):
        page = HowToPage(abstract="howto abstract")
        self.assertEqual(page.abstract, 'howto abstract')

    def test_content(self):
        page = HowToPage(content="<p>howto content</p>")
        self.assertEqual(page.content, '<p>howto content</p>')
