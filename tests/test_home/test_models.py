import http

import pytest
from pytest_django import asserts

from lpld.home import factories as home_factories
from lpld.projects import factories as projects_factories


@pytest.mark.django_db
class TestHomePage:
    def test_page_loads(self, client):
        home_page = home_factories.HomePage()

        response = client.get(path=home_page.get_url())

        assert response.status_code == http.HTTPStatus.OK
        asserts.assertContains(response, home_page.title)

    def test_get_projects(self):
        home_page = home_factories.HomePage()
        project_page_1 = projects_factories.ProjectPage(
            parent=home_page,
            title="Project 1",
            introduction="Introduction 1",
        )
        project_page_2 = projects_factories.ProjectPage(
            parent=home_page,
            title="Project 2",
            introduction="Introduction 2",
        )

        teaser_grid = home_page.projects_teaser_grid

        assert len(teaser_grid.teasers) == 2
        teaser_1 = teaser_grid.teasers[0]
        assert teaser_1.heading == project_page_1.title
        assert teaser_1.introduction == project_page_1.introduction
        assert teaser_1.href == project_page_1.get_url()
        teaser_2 = teaser_grid.teasers[1]
        assert teaser_2.heading == project_page_2.title
        assert teaser_2.introduction == project_page_2.introduction
        assert teaser_2.href == project_page_2.get_url()
