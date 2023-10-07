import dataclasses

from lpld.templates.molecules.teaser import teaser
from lpld import templex


@dataclasses.dataclass(frozen=True)
class TeaserGrid(templex.Templex):
    template="organisms/teaser_grid/teaser-grid.html"
    teasers: list[teaser.Teaser]
