from django import template

from lpld import templex as templex_module

register = template.Library()


@register.simple_tag(takes_context=False)
def templex(obj, **kwargs):
    """Render a templex object."""
    if isinstance(obj, templex_module.Templex):
        return obj.render(**kwargs)
    return str(obj)


