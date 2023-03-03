from django import template
from django.utils import safestring

import sentry_sdk

register = template.Library()


@register.filter
def split(value, splitter=" "):
    return value.split(splitter)


@register.simple_tag()
def sentry_meta():
    return safestring.mark_safe(sentry_sdk.Hub.current.trace_propagation_meta())
