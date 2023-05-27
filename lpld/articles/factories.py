import factory
import wagtail_factories

from lpld.articles import models as articles_models


class ArticlePage(wagtail_factories.PageFactory):
    class Meta:
        model = articles_models.ArticlePage

    title = factory.Sequence(lambda n: f"Blog Page {n}")
    introduction = factory.Faker("paragraph", nb_sentences=3)
