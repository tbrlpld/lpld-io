from django import template

register = template.Library()


@register.filter
def split(value, splitter=" "):
    return value.split(splitter)
