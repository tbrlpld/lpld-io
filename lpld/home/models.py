from django.db import models

from wagtail.admin import edit_handlers
from wagtail.core import fields
from wagtail.core import models as wagtail_models
from wagtail.images import edit_handlers as image_handlers

from lpld.core import blocks


class HomePage(wagtail_models.Page):
    """docstring for HomePage"""

    hero_supertitle = models.CharField(
        blank=True,
        null=False,
        max_length=50,
        help_text="Displayed above the title.",
    )
    hero_title = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        help_text="Title for the main product or service you want to highlight.",
    )
    hero_subtitle = models.CharField(
        blank=True, null=False, max_length=150, help_text="Displayed below the title."
    )

    hero_action_link_text = models.CharField(
        blank=True,
        null=False,
        max_length=50,
        help_text=(
            "Describe the action you want the user to take. "
            'Avoid generic text like "learn more".'
        ),
    )
    hero_action_link_page = models.ForeignKey(
        wagtail_models.Page,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
        help_text="Choose the page on which the user can take the action.",
    )

    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )

    hero_category_teaser_links = fields.StreamField(
        block_types=[("category_teaser_links", blocks.CategoryTeaserLinks())],
        blank=True,
        null=True,
    )

    body = fields.StreamField(
        block_types=[
            ("image_feature_with_teaser_links", blocks.ImageFeatureWithTeaserLinks()),
            ("teaser_links_feature", blocks.TeaserLinksFeature()),
            ("customer_logos", blocks.CustomerLogos()),
            ("call_to_action", blocks.CallToAction()),
        ],
        blank=True,
        null=True,
    )

    content_panels = wagtail_models.Page.content_panels + [
        edit_handlers.MultiFieldPanel(
            heading="Hero",
            children=(
                edit_handlers.FieldPanel(
                    field_name="hero_supertitle", heading="Supertitle"
                ),
                edit_handlers.FieldPanel(field_name="hero_title", heading="Title"),
                edit_handlers.FieldPanel(
                    field_name="hero_subtitle", heading="Subtitle"
                ),
                edit_handlers.MultiFieldPanel(
                    heading="Action link",
                    children=(
                        edit_handlers.FieldPanel(
                            field_name="hero_action_link_text",
                        ),
                        edit_handlers.PageChooserPanel(
                            field_name="hero_action_link_page",
                        ),
                    ),
                ),
                image_handlers.ImageChooserPanel(field_name="hero_image"),
                edit_handlers.StreamFieldPanel(field_name="hero_category_teaser_links"),
            ),
        ),
        edit_handlers.StreamFieldPanel(field_name="body"),
    ]

    template = "pages/home/home.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, args, kwargs)
        context["site_name"] = wagtail_models.Site.find_for_request(request).site_name
        return context
