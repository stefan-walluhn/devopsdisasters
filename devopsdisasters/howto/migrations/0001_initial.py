from django.db import migrations, models
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowToIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(on_delete=models.CASCADE,
                                                  parent_link=True,
                                                  auto_created=True,
                                                  primary_key=True,
                                                  serialize=False,
                                                  to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HowToPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True,
                                                  on_delete=models.CASCADE,
                                                  parent_link=True,
                                                  primary_key=True,
                                                  serialize=False,
                                                  to='wagtailcore.Page')),
                ('abstract', models.TextField()),
                ('content', wagtail.core.fields.RichTextField()),
                ('categories', modelcluster.fields.ParentalManyToManyField(
                    to='categories.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
