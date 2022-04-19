import wagtail_factories

from lpld.home import models as home_models


class HomePage(wagtail_factories.PageFactory):
    class Meta:
        model = home_models.HomePage

    title = "Home"
