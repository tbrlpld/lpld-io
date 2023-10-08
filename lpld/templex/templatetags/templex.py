from typing import Iterable
from django import template
from django.utils import safestring

from lpld import templex as templex_module

register = template.Library()


@register.simple_tag(takes_context=False)
def templex(obj: templex_module.TemplexRenderable, **kwargs) -> safestring.SafeString:
    """
    Render a templex object.

    Iterables of templex objects are also supported. In that case, the templexes
    are rendered and concatenated.

    You can also pass safe strings trough this tag. They will be returned as is.

    """

    if isinstance(obj, safestring.SafeString):
        return obj
    elif isinstance(obj, templex_module.Templex):
        return obj.render(**kwargs)
    elif isinstance(obj, Iterable):
        renders = [
            item.render(**kwargs)
            for item in obj
            if isinstance(item, templex_module.Templex)
        ]
        return safestring.mark_safe("".join(renders))
