from django.db import models
from django.forms import CheckboxSelectMultiple

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from devopsdisasters.categories.models import Category


class HowToIndexPage(Page):
    subpage_types = ['howto.HowToPage']

    def get_context(self, request):
        def _howto_to_categories(categories):
            for category in categories:
                yield (category.name,
                       HowToPage.objects.live().filter(categories=category))

        context = super().get_context(request)

        categories = Category.objects.all()

        context['categories'] = categories
        context['howtos'] = {k: v for k, v in _howto_to_categories(categories)}

        return context


class HowToPage(Page):
    categories = ParentalManyToManyField('categories.Category')
    abstract = models.TextField()
    content = RichTextField()

    parent_page_types = ['howto.HowToIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('categories', widget=CheckboxSelectMultiple),
        FieldPanel('abstract', classname="full"),
        FieldPanel('content', classname="full"),
    ]
