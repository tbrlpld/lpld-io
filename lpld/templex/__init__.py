import dataclasses
import functools
from typing import Type

from django import template as django_template


def templex(template: str):
    """
    Turn class into a templex object.

    The class is turned into a data class and a `render` method is added (if it
    doesn't already exist). Pass the template to render the templex with as a parameter
    to the decorator.

    """

    def wrapper(klass):
        """
        The actual decorator.

        The template that this decorator adds to the class is injected from the
        surrounding scope.

        """
        def render_templex(self):
            """Render the templex by passing its data into the template."""
            templex_template = django_template.loader.get_template(self.template)
            data_dict = dataclasses.asdict(self)
            return templex_template.render(data_dict)

        @functools.wraps(klass)
        def wrap(klass: Type) -> Type:
            # Turn class into a dataclass.
            klass = dataclasses.dataclass(klass)
            # Add the template property to the class if it doesn't already exist.
            if not hasattr(klass, "template"):
                klass.template = template
            # Add the render method to the class if it doesn't already exist.
            if not hasattr(klass, "render"):
                klass.render = render_templex
            return klass

        return wrap(klass)

    return wrapper