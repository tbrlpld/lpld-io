"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import static as static_urls
from django.urls import include, path

from wagtail.admin import urls as wagtail_admin_urls
from wagtail.contrib.sitemaps import views as sitemap_views
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtail_docs_urls

from lpld.core import views as core_views

urlpatterns = [
    path("docs/", include(wagtail_docs_urls)),
    path("lpld-admin/", include(wagtail_admin_urls)),
    path("robots.txt", core_views.RobotsView.as_view()),
    path("sitemap.xml", sitemap_views.sitemap),
]


if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar  # type: ignore

    urlpatterns.extend(
        [
            path("__debug__/", include(debug_toolbar.urls)),
            path("pattern-library/", include("pattern_library.urls")),
        ]
    )
    urlpatterns.extend(
        static_urls.static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )  # type: ignore
    )


sentry_test = getattr(settings, "SENTRY_TEST", False)
if sentry_test:

    def trigger_error(request):
        1 / 0

    urlpatterns.append(path("-/sentry-test/", trigger_error))  # type: ignore

urlpatterns.append(path("", include(wagtail_urls)))
