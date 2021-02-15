from django.conf import settings
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.http import Http404

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel, StreamFieldPanel, MultiFieldPanel)
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index

from devopsdisasters.categories.models import Category
from devopsdisasters.failed.blocks import ExampleCode


class FailedIndexPage(RoutablePageMixin, Page):
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
        context['fails'] = self.get_fails()
        context['categories'] = self.get_all_categories()

        return context

    def get_all_categories(self):
        return Category.objects.all().order_by('name')

    def get_fails(self, category=None):
        fails = FailedPage.objects.live().descendant_of(self)

        if category:
            fails = fails.filter(categories=category)

        return fails.order_by('-first_published_at')

    @route(r'^{}/([\w-]+)/$'.format(settings.DEVOPSDISASTERS_CATEGORY_ROUTE))
    def category(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404("Category does not exist")

        return self.render(request, context_overrides={
            'fails': self.get_fails(category=category)
        })


class FailedPage(Page):
    quote = models.CharField(max_length=250, blank=True)
    categories = ParentalManyToManyField('categories.Category', blank=True)
    fail = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('example_code', ExampleCode()),
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

    def get_context(self, request):
        context = super().get_context(request)
        context['recent_fails'] = (self.get_siblings().live()
                                   .order_by('-first_published_at')[:5])
        context['categories'] = Category.objects.all()

        return context
