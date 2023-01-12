import pytest

from lpld.projects import factories


@pytest.mark.django_db
class TestProjectPageFactory:
    def test_factory(self):
        factories.ProjectPage()

        assert True
