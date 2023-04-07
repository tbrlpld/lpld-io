import http

import pytest
from pytest_django import asserts

from lpld.home import factories as home_factories
from lpld.blog import factories


@pytest.mark.django_db
class TestBlogIndexPage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        page = factories.BlogIndexPage(parent=home_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)


@pytest.mark.django_db
class TestBlogPage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        index_page = factories.BlogIndexPage(parent=home_page)
        page = factories.BlogPage(parent=index_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)
