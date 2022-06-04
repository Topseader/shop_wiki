from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=False)
@stringfilter
def prettify(value):
    return value.replace("_", " ")