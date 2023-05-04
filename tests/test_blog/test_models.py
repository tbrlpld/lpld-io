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
        child_page = factories.BlogPostPage(parent=page)

        assert page.get_index_entries() == tuple(
            [
                {
                    "title": child_page.title,
                    "url": child_page.get_url(),
                },
            ]
        )

    def test_get_index_entries_only_returns_published_pages(self):
        index_page = factories.BlogIndexPage()
        factories.BlogPostPage(parent=index_page, live=False)
        published_post = factories.BlogPostPage(parent=index_page)

        entries = index_page.get_index_entries()

        assert entries == tuple(
            [
                {
                    "title": published_post.title,
                    "url": published_post.get_url(),
                },
            ]
        )

    def test_get_index_entries_only_returns_public_pages(self):
        index_page = factories.BlogIndexPage()
        private_post = factories.BlogPostPage(parent=index_page)
        private_post.view_restrictions.create(
            restriction_type="password",
            password="password",
        )
        public_post = factories.BlogPostPage(parent=index_page)

        entries = index_page.get_index_entries()

        assert entries == tuple(
            [
                {
                    "title": public_post.title,
                    "url": public_post.get_url(),
                },
            ]
        )


@pytest.mark.django_db
class TestBlogPostPage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()
        index_page = factories.BlogIndexPage(parent=home_page)
        page = factories.BlogPostPage(parent=index_page)

        response = client.get(path=page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, page.title)
