from typing import TYPE_CHECKING, Union, Iterable
import abc
import dataclasses

from django.template import loader

if TYPE_CHECKING:
    from django.utils import safestring


class Templex(abc.ABC):
    template: str

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'template'):
            raise TypeError(
                f"Templex subclass '{cls.__name__}' must set 'template' attribute."
            )

    def get_template(self) -> str:
        return self.template

    def get_context_data(self) -> dict:
        """
        Return a dictionary of data to be passed to the template.

        By default, this class attempts to convert the object itself into a dictionary.
        """
        if dataclasses.is_dataclass(self):
            # Shallow copy to avoid the resolution of nested templexes. We need the
            # nested templexes to stay templexes so that they keep their render method
            # and instead of being turned into plain dicts.
            return dict(
                (field.name, getattr(self, field.name))
                for field in dataclasses.fields(self)
            )
        else:
            return self.__dict__.copy()

    def render(self, **kwargs: dict) -> "safestring.SafeString":
        """
        Render the templex by passing its data into the template.

        The context can be extended by passing keyword arguments to this method.

        """
        data_dict = self.get_context_data()
        if kwargs:
            data_dict.update(kwargs)
        templex_template = loader.get_template(self.get_template())
        return templex_template.render(data_dict)


TemplexRenderable = Union[str, Templex, Iterable[Templex]]
