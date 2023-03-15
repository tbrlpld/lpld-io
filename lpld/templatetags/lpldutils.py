from django import template
from django.utils import safestring

import sentry_sdk

register = template.Library()


@register.filter
def split(value, splitter=" "):
    return value.split(splitter)


@register.simple_tag()
def sentry_meta():
    """
    Generate meta tags for Sentry trace propagation.

    Trace propagation is needed for Sentry to be able to link transactions and errors
    together and to be able to show the full trace (from backend to frontend) in the
    Sentry UI.

    """
    meta = sentry_sdk.Hub.current.trace_propagation_meta()
    return safestring.mark_safe(meta)
