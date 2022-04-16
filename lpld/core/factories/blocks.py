import wagtail_factories

from lpld.core import blocks


class ActionLink(wagtail_factories.StructBlockFactory):
    class Meta:
        model = blocks.ActionLink


class CallToAction(wagtail_factories.StructBlockFactory):
    class Meta:
        model = blocks.CallToAction


class CustomerLogos(wagtail_factories.StructBlockFactory):
    class Meta:
        model = blocks.CustomerLogos


class TeaserLink(wagtail_factories.StructBlockFactory):
    class Meta:
        model = blocks.TeaserLink


class CategoryTeaserLinks(wagtail_factories.StructBlockFactory):
    class Meta:
        model = blocks.CategoryTeaserLinks


class TeaserLinksFeature(wagtail_factories.StructBlockFactory):
    class Meta:
        model = blocks.TeaserLinksFeature


class ImageFeatureWithTeaserLinks(wagtail_factories.StructBlockFactory):
    class Meta:
        model = blocks.ImageFeatureWithTeaserLinks


def generate_block(*, block_type: str, value: dict):
    """
    Create the dictionary that can be passed into a StreamField.


    """
    return {
        "type": block_type,
        "value": value,
    }
