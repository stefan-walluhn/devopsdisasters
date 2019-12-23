from django.db import models
from django.forms import CheckboxSelectMultiple

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel, StreamFieldPanel, MultiFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index


class FailedIndexPage(Page):
    subpage_types = ['failed.FailedPage']

    intro = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['fails'] = (self.get_children().live()
                            .order_by('-first_published_at'))
        return context


class FailedPage(Page):
    quote = models.CharField(max_length=250, blank=True)
    categories = ParentalManyToManyField('categories.Category', blank=True)
    fail = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('example_code', blocks.StructBlock([
            ('code', blocks.BlockQuoteBlock()),
            ('source', blocks.URLBlock(required=False)),
        ])),
    ])
    lessons_learned = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField('fail'),
        index.SearchField('lessons_learned'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('categories', widget=CheckboxSelectMultiple),
        MultiFieldPanel([
            FieldPanel('quote'),
            StreamFieldPanel('fail'),
            FieldPanel('lessons_learned'),
        ], heading="content"),
    ]

    parent_page_types = ['failed.FailedIndexPage']
    subpage_types = []
