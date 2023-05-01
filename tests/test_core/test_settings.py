import pytest
import wagtail_factories

from lpld.core.factories import models as model_factories
from lpld.core import settings as settings_utils


@pytest.mark.django_db
class TestGetPrimaryNavigationLinks:
    @pytest.fixture
    def primary_nav_setting(self, settings):
        settings.ALLOWED_HOSTS = ["example.com"]
        site = wagtail_factories.SiteFactory(hostname="example.com")
        primary_nav_setting = model_factories.PrimaryNavigationSettingFactory(site=site)
        return primary_nav_setting

    def test_contains_project_and_contact_links(self, rf, primary_nav_setting):
        """Making sure these two links are returned even without any other links defined."""
        request = rf.get("/", HTTP_HOST=primary_nav_setting.site.hostname)

        links = settings_utils.get_primary_navigation_links(request)

        assert len(links) == 2
        assert links[0]["text"] == "Projects"
        assert links[1]["text"] == "Contact"

    def test_contains_links_from_setting(self, rf, primary_nav_setting):
        """Making sure links from the setting are returned."""
        link = model_factories.PrimaryNavigationLinkFactory(primary_navigation=primary_nav_setting)
        request = rf.get("/", HTTP_HOST=primary_nav_setting.site.hostname)

        links = settings_utils.get_primary_navigation_links(request)

        assert len(links) == 3
        assert links[0]["text"] == link.text
        assert links[0]["url"] == link.url
