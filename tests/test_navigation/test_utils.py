import pytest
import wagtail_factories

from lpld.navigation import factories as nav_factories
from lpld.navigation import utils as nav_utils


@pytest.mark.django_db
class TestGetPrimaryNavigationLinks:
    @pytest.fixture
    def primary_nav_setting(self, settings):
        settings.ALLOWED_HOSTS = ["example.com"]
        site = wagtail_factories.SiteFactory(hostname="example.com")
        primary_nav_setting = nav_factories.PrimaryNavigationSettingFactory(site=site)
        return primary_nav_setting

    def test_contains_project_and_contact_links(self, rf, primary_nav_setting):
        """Ensure these two links are returned even without any other links defined."""
        request = rf.get("/", HTTP_HOST=primary_nav_setting.site.hostname)

        links = nav_utils.get_primary_navigation_links(request)

        assert len(links) == 2
        assert links[0].text == "Projects"
        assert links[0].href == "/#projects"
        assert links[1].text == "Contact"
        assert links[1].href == "#contact"

    def test_contains_links_from_setting(self, rf, primary_nav_setting):
        """Making sure links from the setting are returned."""
        link = nav_factories.PrimaryNavigationLinkFactory(
            primary_navigation=primary_nav_setting
        )
        request = rf.get("/", HTTP_HOST=primary_nav_setting.site.hostname)

        links = nav_utils.get_primary_navigation_links(request)

        assert len(links) == 3
        assert links[0] == link
