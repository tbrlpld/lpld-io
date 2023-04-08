import http

import pytest
from pytest_django import asserts

from lpld.blog import factories
from lpld.home import factories as home_factories


@pytest.mark.django_db
class TestBlogIndexPage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        page = factories.BlogIndexPage(parent=home_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)

    def test_get_index_entries_no_child_pages(self):
        page = factories.BlogIndexPage()

        assert page.get_index_entries() == tuple()

    def test_get_index_entries_with_child_pages(self):
        page = factories.BlogIndexPage()
        child_page = factories.BlogPage(parent=page)

        assert page.get_index_entries() == tuple(
            [
                {
                    "title": child_page.title,
                    "url": child_page.get_url(),
                },
            ]
        )


@pytest.mark.django_db
class TestBlogPage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        index_page = factories.BlogIndexPage(parent=home_page)
        page = factories.BlogPage(parent=index_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)
