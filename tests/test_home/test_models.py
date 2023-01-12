import http

import pytest
import wagtail_factories

from lpld.home import factories


@pytest.mark.django_db
class TestHomePage:
    def test_page_loads(self, client):
        home_page = factories.HomePage()
        wagtail_factories.SiteFactory(root_page=home_page)

        response = client.get(path=home_page.get_url())

        assert response.status_code == http.HTTPStatus.OK
