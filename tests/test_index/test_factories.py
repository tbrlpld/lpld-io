import pytest

from lpld.index import factories as index_factories


@pytest.mark.django_db
class TestIndexPageFactory:
    def test_factory(self):
        index_factories.IndexPage()

        assert True
