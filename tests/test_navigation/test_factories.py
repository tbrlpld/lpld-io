import pytest
from wagtail import models as wagtail_models

from lpld.navigation import factories as nav_factories
from lpld.navigation import models as nav_models


@pytest.mark.django_db
class TestPrimaryNavigationSettingFactory:
    def test_factory(self):
        setting = nav_factories.PrimaryNavigationSettingFactory()

        assert setting.site
        assert isinstance(setting.site, wagtail_models.Site)


@pytest.mark.django_db
class TestNavigationLinkFactory:
    def test_factory(self):
        link = nav_factories.PrimaryNavigationLinkFactory()

        assert link.page
        assert isinstance(link.page, wagtail_models.Page)
        assert link.primary_navigation
        assert isinstance(
            link.primary_navigation,
            nav_models.PrimaryNavigationSetting,
        )

    def test_can_set_text_override(self):
        link = nav_factories.PrimaryNavigationLinkFactory(text_override="foo")

        assert link.text_override == "foo"
