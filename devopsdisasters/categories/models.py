from django.db import models
from django.dispatch import receiver
from django.template.defaultfilters import slugify


from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet


@register_snippet
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(unique=True, max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    intro = RichTextField()

    panels = [
        FieldPanel('name'),
        FieldPanel('intro'),
    ]

    def __str__(self):
        return self.name


@receiver(models.signals.pre_save, sender=Category)
def generate_slug(instance, **kwargs):
    instance.slug = slugify(instance.name)
