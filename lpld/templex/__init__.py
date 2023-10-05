import dataclasses
import functools
from typing import Callable, Protocol, Type, cast

from django.template import loader


def templex(template: str) -> Callable:
    """
    Turn class into a templex object.

    The class is turned into a data class and a `render` method is added (if it
    doesn't already exist). Pass the template to render the templex with as a parameter
    to the decorator.

    """

    def wrapper(klass: Type) -> TemplexProtocol:
        """
        The actual decorator.

        The template that this decorator adds to the class is injected from the
        surrounding scope.

        """
        def render_templex(self, **kwargs: dict) -> str:
            """
            Render the templex by passing its data into the template.

            The context can be extended by passing keyword arguments to this method.

            """
            templex_template = loader.get_template(self.template)
            # Shallow copy to avoid the resolution of nested templexes. We need the
            # nested templexes to stay templexes so that they can be rendered later.
            data_dict = dict(
                (field.name, getattr(self, field.name))
                for field in dataclasses.fields(self)
            )
            if kwargs:
                data_dict.update(kwargs)
            return templex_template.render(data_dict)

        @functools.wraps(klass)
        def wrap(klass: Type) -> TemplexProtocol:
            # Turn class into a dataclass.
            dataklass = dataclasses.dataclass(klass)
            # Add the template property to the class if it doesn't already exist.
            if not hasattr(dataklass, "template"):
                dataklass.template = template
            # Add the render method to the class if it doesn't already exist.
            if not hasattr(dataklass, "render"):
                dataklass.render = render_templex
            return cast(TemplexProtocol, dataklass)

        return wrap(klass)

    return wrapper


@dataclasses.dataclass
class DataclassProtocol(Protocol):
    pass

class TemplexProtocol(DataclassProtocol):
    template: str
    render: Callable
