from typing import Iterable, Union
import dataclasses


from lpld import templex


@dataclasses.dataclass(frozen=True)
class Prose(templex.Templex):
    template = "organisms/prose/prose.html"

    children: Union[str, template.Templex, Iterable[templex.Templex]]
