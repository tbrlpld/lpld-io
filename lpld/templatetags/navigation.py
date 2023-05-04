from django import template

from lpld.navigation import utils as navigation_utils

register = template.Library()


@register.inclusion_tag(
    "molecules/navigation/primary-navigation.html",
    takes_context=True,
)
def primary_navigation(context):
    links = navigation_utils.get_primary_navigation_links(context["request"])
    return {"links": links}
