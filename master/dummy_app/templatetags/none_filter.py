# your_app/templatetags/none_filter.py
from django import template

register = template.Library()

@register.filter
def none_filter(value):
    return value if value is not None else ''
