import dataclasses

from django.apps import apps

from lpld.templates.molecules.teaser import teaser
from lpld import templex


@dataclasses.dataclass(frozen=True)
class TeaserGrid(templex.Templex):
    template="organisms/teaser_grid/teaser-grid.html"
    teasers: list[teaser.Teaser]

    @classmethod
    def from_project_pages(cls) -> "TeaserGrid":
        ProjectPage = apps.get_model("projects", "ProjectPage")

        return cls(
            teasers=[
                teaser.Teaser.from_project_page(project_page)
                for project_page in ProjectPage.objects.live().public()
            ]
        )
