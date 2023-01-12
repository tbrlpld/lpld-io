import factory
import wagtail_factories

from lpld.home import models as home_models


class HomePage(wagtail_factories.PageFactory):
    class Meta:
        model = home_models.HomePage

    title = "Home"
    introduction = factory.Faker("sentences", nb=3)
    profile_image = factory.SubFactory(wagtail_factories.ImageFactory)

    @factory.post_generation
    def create_site_with_homepage_as_root(obj, create, extracted, **kwargs):
        if not create:
            return
        site = wagtail_factories.SiteFactory(root_page=obj, is_default_site=True)
        return site
