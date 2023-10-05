import dataclasses

from lpld.templates.molecules.teaser import teaser
from lpld import templex


@templex.templex(template="organisms/teaser_grid/teaser-grid.html")
@dataclasses.dataclass
class TeaserGrid:
    teasers: list[teaser.Teaser]
