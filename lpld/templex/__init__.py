import abc
import dataclasses

from django.template import loader


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

    def render(self, **kwargs: dict) -> str:
        """
        Render the templex by passing its data into the template.

        The context can be extended by passing keyword arguments to this method.

        """
        if dataclasses.is_dataclass(self):
            # Shallow copy to avoid the resolution of nested templexes. We need the
            # nested templexes to stay templexes so that they keep their render method
            # and instead of being turned into plain dicts.
            data_dict = dict(
                (field.name, getattr(self, field.name))
                for field in dataclasses.fields(self)
            )
        else:
            data_dict = self.__dict__.copy()
        if kwargs:
            data_dict.update(kwargs)
        templex_template = loader.get_template(self.get_template())
        return templex_template.render(data_dict)
