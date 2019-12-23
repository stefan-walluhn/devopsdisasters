from django import template


register = template.Library()


@register.filter('value_from_dict')
def value_from_dict(d, key=None):
    if not key: return None
    return d.get(key, None)
