import pytest
import wagtail_factories

from lpld.core.factories import models as model_factories
from lpld.core import settings as settings_utils


@pytest.mark.django_db
class TestGetPrimaryNavigationLinks:
    def test_contains_project_and_contact_links(self, rf):
        """Making sure these two links are returned even without any other links defined."""
        setting = model_factories.PrimaryNavigationSettingFactory()
        request = rf.get("/", HTTP_HOST=setting.site.hostname)

        links = settings_utils.get_primary_navigation_links(request)

        assert len(links) == 2
        assert links[0]["text"] == "Projects"
        assert links[1]["text"] == "Contact"

    def test_contains_links_from_setting(self, rf, settings):
        """Making sure links from the setting are returned."""
        settings.ALLOWED_HOSTS = ["example.com"]
        site = wagtail_factories.SiteFactory(hostname="example.com")
        setting = model_factories.PrimaryNavigationSettingFactory(site=site)
        link = model_factories.PrimaryNavigationLinkFactory(primary_navigation=setting)
        request = rf.get("/", HTTP_HOST=setting.site.hostname)

        links = settings_utils.get_primary_navigation_links(request)

        assert len(links) == 3
        assert links[0]["text"] == link.text
        assert links[0]["url"] == link.url
