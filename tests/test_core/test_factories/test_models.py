import pytest
from wagtail import models as wagtail_models


from lpld.core.factories import models as model_factories


@pytest.mark.django_db
class TestNavigationLinkFactory:
    def test_factory(self):
        link = model_factories.PrimaryNavigationLinkFactory()

        assert link.page
        assert isinstance(link.page, wagtail_models.Page)
