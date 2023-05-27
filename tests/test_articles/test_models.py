import http

import pytest
from pytest_django import asserts

from lpld.articles import factories as articles_factories
from lpld.home import factories as home_factories
from lpld.index import factories as index_factories


@pytest.mark.django_db
class TestArticlePage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        index_page = index_factories.IndexPage(parent=home_page)
        page = articles_factories.ArticlePage(parent=index_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)
