from typing import NamedTuple

from django.apps import apps


class Link(NamedTuple):
    text: str
    href: str


def get_primary_navigation_links(request):
    links = []

    PrimaryNavigationSetting = apps.get_model("navigation.PrimaryNavigationSetting")
    links.extend(list(PrimaryNavigationSetting.for_request(request).links.all()))
    links.extend(
        [
            Link(text="Projects", href="/#projects"),
            Link(text="Contact", href="#contact"),
        ]
    )
    return links
