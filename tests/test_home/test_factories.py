import pytest

from lpld.home import factories


@pytest.mark.django_db
class TestHomePageFactory:
    def test_factory(self):
        factories.HomePage()

        assert True
