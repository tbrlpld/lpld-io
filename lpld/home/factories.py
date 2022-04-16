import factory
import wagtail_factories

from lpld.home import models as home_models


class HomePage(wagtail_factories.PageFactory):
    class Meta:
        model = home_models.HomePage

    title = "Home"

    hero_supertitle = "We manufacture"
    hero_title = "DAN-EX"
    hero_subtitle = "America's leading double block and bleed valve"

    hero_action_link_text = "Request pricing"
    hero_action_link_page = None

    hero_image = factory.SubFactory(wagtail_factories.ImageFactory)
