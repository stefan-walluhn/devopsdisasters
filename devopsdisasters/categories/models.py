from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet


@register_snippet
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=250)
    intro = RichTextField()

    panels = [
        FieldPanel('name'),
        FieldPanel('intro'),
    ]

    def __str__(self):
        return self.name
