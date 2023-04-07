import pytest

from lpld.blog import factories


@pytest.mark.django_db
class TestBlogIndexPageFactory:
    def test_factory(self):
        factories.BlogIndexPage()

        assert True


@pytest.mark.django_db
class TestBlogPageFactory:
    def test_factory(self):
        factories.BlogPage()

        assert True
