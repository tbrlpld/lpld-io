import pytest

from lpld.blog import factories


@pytest.mark.django_db
class TestBlogIndexPageFactory:
    def test_factory(self):
        factories.BlogIndexPage()

        assert True


@pytest.mark.django_db
class TestBlogPostPageFactory:
    def test_factory(self):
        factories.BlogPostPage()

        assert True
