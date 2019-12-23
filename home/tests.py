from wagtail.tests.utils import WagtailPageTests

from home.models import HomePage


class TestHomePage(WagtailPageTests):
    def test_parent_page_types(self):
        self.assertAllowedParentPageTypes(HomePage, [])
