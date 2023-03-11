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

    # noqa: E501
    The meta generation is copied from: https://github.com/getsentry/sentry-python/blob/ff60906fcb9af3db9cda245288f2e49f70ee432f/sentry_sdk/hub.py#L737-L748b
    This is needed because the `trace_propagation_meta` method is not yet released.

    """
    meta = ""
    for name, content in sentry_sdk.Hub.current.iter_trace_propagation_headers():
        meta += f'<meta name="{name}" content="{content}">'
    return safestring.mark_safe(meta)
