import dataclasses

from lpld import templex


@dataclasses.dataclass(frozen=True)
class Section(templex.Templex):
    template="molecules/section/section.html"
    content: list[templex.Templex]
    html_id: str = ""
    html_class: str = ""

