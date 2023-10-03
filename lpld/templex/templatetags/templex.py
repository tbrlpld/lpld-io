from django import template

register = template.Library()


@register.simple_tag(takes_context=False)
def templex(templex_obj, **kwargs):
    """Render a templex object."""
    return templex_obj.render(**kwargs)


