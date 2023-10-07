import abc
import dataclasses

from django.template import loader


class Templex(abc.ABC):
    @property
    @abc.abstractmethod
    def template(self) -> str:
        """
        Subclassed must define a template attribute.

        Will raise an error like this if not defined:
        TypeError: Can't instantiate abstract class TeaserGrid with abstract methods
        template

        """
        pass

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
