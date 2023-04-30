import factory
import wagtail_factories

from lpld.core import models as core_models


class PrimaryNavigationLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = core_models.PrimaryNavigationLink

    page = factory.SubFactory(wagtail_factories.PageFactory)
