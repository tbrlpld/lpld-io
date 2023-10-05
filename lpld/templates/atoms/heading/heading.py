import dataclasses
from typing import Optional

from lpld import templex


@templex.templex(template="atoms/heading/heading.html")
@dataclasses.dataclass
class Heading:
    level: Optional[int]
    size: str = ""
    extra_class: str = ""
    text: str = ""
