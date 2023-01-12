import factory
import wagtail_factories

from lpld.projects import models as projects_models


class ProjectPage(wagtail_factories.PageFactory):
    class Meta:
        model = projects_models.ProjectPage

    title = factory.Sequence(lambda n: f"Project {n}")
    image = factory.SubFactory(wagtail_factories.ImageFactory)
    image_shadow = True

    introduction = factory.Faker("sentences", nb=3)
    description = factory.Faker("sentences", nb=5)

    repo_url = factory.Faker("uri")
    demo_url = factory.Faker("uri")
