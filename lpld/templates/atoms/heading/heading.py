from typing import Optional

from lpld import templex


@templex.templex(template="atoms/heading/heading.html")
class Heading:
    level: Optional[int]
    size: str = ""
    extra_classes: str = ""
    text: str = ""
