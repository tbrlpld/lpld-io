import dataclasses

from django import template

register = template.Library()


@register.simple_tag(takes_context=False)
def include_templex(templex):
    templex_template = template.loader.get_template(templex.template)
    return templex_template.render(dataclasses.asdict(templex))
