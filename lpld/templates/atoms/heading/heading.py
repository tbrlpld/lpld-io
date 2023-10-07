import dataclasses
from typing import Optional

from lpld import templex


@dataclasses.dataclass
class Heading(templex.Templex):
    template = "atoms/heading/heading.html"

    level: Optional[int]
    size: str = ""
    extra_class: str = ""
    text: str = ""


