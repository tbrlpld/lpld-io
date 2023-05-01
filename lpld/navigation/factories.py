import factory
import wagtail_factories

from lpld.navigation import models as nav_models


class PrimaryNavigationSettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = nav_models.PrimaryNavigationSetting

    site = factory.SubFactory(wagtail_factories.SiteFactory)


class PrimaryNavigationLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = nav_models.PrimaryNavigationLink

    primary_navigation = factory.SubFactory(PrimaryNavigationSettingFactory)
    page = factory.SubFactory(wagtail_factories.PageFactory)
