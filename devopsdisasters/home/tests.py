from wagtail.tests.utils import WagtailPageTests

from devopsdisasters.home.models import HomePage


class TestHomePage(WagtailPageTests):
    def test_parent_page_types(self):
        self.assertAllowedParentPageTypes(HomePage, [])
