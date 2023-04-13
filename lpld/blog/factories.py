import factory
import wagtail_factories

from lpld.blog import models as blog_models


class BlogIndexPage(wagtail_factories.PageFactory):
    class Meta:
        model = blog_models.BlogIndexPage

    title = factory.Sequence(lambda n: f"Blog {n}")


class BlogPage(wagtail_factories.PageFactory):
    class Meta:
        model = blog_models.BlogPage

    title = factory.Sequence(lambda n: f"Blog Page {n}")
    introduction = factory.Faker("paragraph", nb_sentences=3)
