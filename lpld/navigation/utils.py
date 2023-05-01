from django.apps import apps


def get_primary_navigation_links(request):
    links = []

    PrimaryNavigationSetting = apps.get_model("navigation.PrimaryNavigationSetting")
    links.extend(
        [
            {
                "text": link.text,
                "url": link.url,
            }
            for link in PrimaryNavigationSetting.for_request(request).links.all()
        ]
    )

    links.append(
        {
            "text": "Projects",
            "url": "/#projects",
        }
    )
    links.append(
        {
            "text": "Contact",
            "url": "#contact",
        }
    )
    return links
