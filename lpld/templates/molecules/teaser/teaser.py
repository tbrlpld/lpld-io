import dataclasses
from typing import Optional

from wagtail.images import models as images_models
from wagtailmedia import models as media_models

from lpld import templex



@dataclasses.dataclass(frozen=True)
class Teaser(templex.Templex):
    template="molecules/teaser/teaser.html"

    heading: str
    introduction: str
    href: str
    image: Optional[images_models.AbstractImage]
    image_shadow: bool
    video: Optional[media_models.AbstractMedia]
