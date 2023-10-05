import dataclasses

from lpld import templex


@templex.templex(template="molecules/section/section.html")
@dataclasses.dataclass
class Section:
    content: list[templex.TemplexProtocol]
    html_id: str = ""
    html_class: str = ""

