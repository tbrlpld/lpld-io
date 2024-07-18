import http

import pytest
from pytest_django import asserts

from lpld.articles import factories as articles_factories
from lpld.home import factories as home_factories
from lpld.index import factories as index_factories


@pytest.mark.django_db
class TestIndexPage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        page = index_factories.IndexPage(parent=home_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)

    def test_get_index_entries_no_child_pages(self):
        page = index_factories.IndexPage()

        assert page.get_index_entries() == tuple()

    def test_get_index_entries_with_child_pages(self):
        page = index_factories.IndexPage()
        child_page = articles_factories.ArticlePage(parent=page)

        assert page.get_index_entries() == tuple(
            [
                {
                    "text": child_page.title,
                    "href": child_page.get_url(),
                },
            ]
        )

    def test_get_index_entries_only_returns_published_pages(self):
        index_page = index_factories.IndexPage()
        articles_factories.ArticlePage(parent=index_page, live=False)
        published_post = articles_factories.ArticlePage(parent=index_page)

        entries = index_page.get_index_entries()

        assert entries == tuple(
            [
                {
                    "text": published_post.title,
                    "href": published_post.get_url(),
                },
            ]
        )

    def test_get_index_entries_only_returns_public_pages(self):
        index_page = index_factories.IndexPage()
        private_post = articles_factories.ArticlePage(parent=index_page)
        private_post.view_restrictions.create(
            restriction_type="password",
            password="password",
        )
        public_post = articles_factories.ArticlePage(parent=index_page)

        entries = index_page.get_index_entries()

        assert entries == tuple(
            [
                {
                    "text": public_post.title,
                    "href": public_post.get_url(),
                },
            ]
        )
