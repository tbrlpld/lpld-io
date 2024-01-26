import dataclasses
from typing import Union, Iterable

from lpld import templex


@dataclasses.dataclass
class Heading(templex.Templex):
    template = "atoms/heading/heading.html"

    text: str
    level: int = 1
    size: str = ""
    extra_class: str = ""


