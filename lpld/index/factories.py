import factory
import wagtail_factories

from lpld.index import models as index_models


class IndexPage(wagtail_factories.PageFactory):
    class Meta:
        model = index_models.IndexPage

    title = factory.Sequence(lambda n: f"Blog {n}")
