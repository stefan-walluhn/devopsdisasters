from django.utils.safestring import mark_safe

from wagtail.core import blocks

from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name


class ExampleCodeValue(blocks.StructValue):
    def formatted_code(self):
        language = self.get('language')
        code = self.get('code')

        lexer = get_lexer_by_name(language)
        formatter = get_formatter_by_name(
            'html', style='colorful', cssclass="example_code")

        render_content = highlight(code, lexer, formatter)

        return mark_safe(render_content)


class ExampleCode(blocks.StructBlock):
    language = blocks.ChoiceBlock(
        choices=(
            ('cpp', 'C++'),
            ('java', 'Java'),
            ('python3', 'Python 3'),
            ('bash', 'Bash/Shell'),
            ('javascript', 'Javascript'),
            ('css', "CSS"),
            ('html', "HTML"),
            ('nginx', "Nginx configuration file"),
            ('jinja', "Jinja"),
            ('docker', "Docker"),
            ('yaml', "YAML"),
            ('json', "JSON"),
        ),
        blank=False,
        null=False,
        default="python3"
    )
    code = blocks.TextBlock()
    source = blocks.URLBlock(required=False)

    class Meta:
        icon = "cose"
        template = "blocks/example_code.html"
        value_class = ExampleCodeValue
