import pytest
from wagtail import models as wagtail_models

from lpld.core import models as core_models
from lpld.core.factories import models as model_factories


@pytest.mark.django_db
class TestPrimaryNavigationSettingFactory:
    def test_factory(self):
        setting = model_factories.PrimaryNavigationSettingFactory()

        assert setting.site
        assert isinstance(setting.site, wagtail_models.Site)


@pytest.mark.django_db
class TestNavigationLinkFactory:
    def test_factory(self):
        link = model_factories.PrimaryNavigationLinkFactory()

        assert link.page
        assert isinstance(link.page, wagtail_models.Page)
        assert link.primary_navigation
        assert isinstance(link.primary_navigation, core_models.PrimaryNavigationSetting)

    def test_can_set_text_override(self):
        link = model_factories.PrimaryNavigationLinkFactory(text_override="foo")

        assert link.text_override == "foo"
