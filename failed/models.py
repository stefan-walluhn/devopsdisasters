from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class FailedIndexPage(Page):
    subpage_types = ['failed.FailedPage']

    intro = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class FailedPage(Page):
    parent_page_types = ['failed.FailedIndexPage']

    fail = RichTextField()
    lessons_learned = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('fail', classname="full"),
        FieldPanel('lessons_learned', classname="full"),
    ]
