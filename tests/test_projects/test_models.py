import http

import pytest
from pytest_django import asserts

from lpld.home import factories as home_factories
from lpld.projects import factories


@pytest.mark.django_db
class TestProjectPage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        page = factories.ProjectPage(parent=home_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)
