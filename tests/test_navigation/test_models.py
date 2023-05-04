import pytest
import wagtail_factories

from lpld.navigation import factories as nav_factories


@pytest.mark.django_db
class TestPrimaryNavigationLink:
    def test_text_and_url_from_page(self):
        page = wagtail_factories.PageFactory(title="foo")
        link = nav_factories.PrimaryNavigationLinkFactory(page=page)

        assert link.text == "foo"
        assert link.href == page.get_url()

    def test_text_override(self):
        link = nav_factories.PrimaryNavigationLinkFactory(text_override="bar")

        assert link.text == "bar"
