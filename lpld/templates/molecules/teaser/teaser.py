import dataclasses
from typing import Optional, TYPE_CHECKING

from wagtail.images import models as images_models
from wagtailmedia import models as media_models

from lpld import templex

if TYPE_CHECKING:
    from lpld.projects import models as projects_models


@dataclasses.dataclass(frozen=True)
class Teaser(templex.Templex):
    template="molecules/teaser/teaser.html"

    heading: str
    introduction: str
    href: str
    image: Optional[images_models.AbstractImage]
    image_shadow: bool
    video: Optional[media_models.AbstractMedia]

    @classmethod
    def from_project_page(cls, project_page: "projects_models.ProjectPage") -> "Teaser":
        return cls(
            heading=project_page.title,
            introduction=project_page.introduction,
            href=project_page.get_url(),
            image=project_page.image,
            image_shadow=project_page.image_shadow,
            video=project_page.video,
        )
