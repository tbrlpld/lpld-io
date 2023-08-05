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

        projects = home_page.project_teasers

        assert len(projects) == 2
        project_1 = projects[0]
        assert project_1.title == project_page_1.title
        assert project_1.introduction == project_page_1.introduction
        assert project_1.href == project_page_1.get_url()
        project_2 = projects[1]
        assert project_2.title == project_page_2.title
        assert project_2.introduction == project_page_2.introduction
        assert project_2.href == project_page_2.get_url()
