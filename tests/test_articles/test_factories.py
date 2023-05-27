import pytest

from lpld.articles import factories as articles_factories


@pytest.mark.django_db
class TestArticlePageFactory:
    def test_factory(self):
        articles_factories.ArticlePage()

        assert True
