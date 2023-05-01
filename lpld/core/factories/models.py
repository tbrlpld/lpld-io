import factory
import wagtail_factories

from lpld.core import models as core_models


class PrimaryNavigationSettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = core_models.PrimaryNavigationSetting

    site = factory.SubFactory(wagtail_factories.SiteFactory)


class PrimaryNavigationLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = core_models.PrimaryNavigationLink

    primary_navigation = factory.SubFactory(PrimaryNavigationSettingFactory)
    page = factory.SubFactory(wagtail_factories.PageFactory)
