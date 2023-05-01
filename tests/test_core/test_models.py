import pytest
from wagtail import test as wagtail_test
import wagtail_factories


from lpld.core.factories import models as model_factories


@pytest.mark.django_db
class TestPrimaryNavigationLink:
    def test_text_and_url_from_page(self):
        page = wagtail_factories.PageFactory(title="foo")
        link = model_factories.PrimaryNavigationLinkFactory(page=page)

        assert link.text == "foo"
        assert link.url == page.url

    def test_text_override(self):
        link = model_factories.PrimaryNavigationLinkFactory(text_override="bar")

        assert link.text == "bar"
