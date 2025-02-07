# master/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def checkNone(value):
    return value if value is not None else ''
