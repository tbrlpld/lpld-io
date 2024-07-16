from django.db import models
from django.utils import html as html_utils

from wagtail import fields
from wagtail import images as wagtail_images
from wagtail.admin import panels

from lpld.core import models as core_models
from lpld.core import blocks as core_blocks


class HomePage(core_models.BasePage):
    """docstring for HomePage"""

    max_count = 1
    template = "pages/home/home.html"

    subtitle = models.CharField(
        max_length=50,
        blank=True,
        null=False,
    )
    introduction = fields.RichTextField(features=["link"], null=True, blank=True)
    profile_image = models.ForeignKey(
        wagtail_images.get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    body = fields.StreamField(
        block_types=[
            ("section", core_blocks.SectionBlock()),
        ],
        null=False,
        blank=True,
        use_json_field=True,
    )


    content_panels = core_models.BasePage.content_panels + [
        panels.FieldPanel("subtitle"),
        panels.FieldPanel("introduction"),
        panels.FieldPanel("profile_image"),
        panels.FieldPanel("body"),
    ]

    def get_title_tag_parts(self) -> list[str]:
        return [self.title, self.subtitle, self.get_title_tag_last_part()]

    def get_meta_description(self):
        return self.search_description or self.get_introduction_without_tags() or ""

    def get_introduction_without_tags(self):
        """Return introduction but without the HTMl tags."""
        return html_utils.strip_tags(self.introduction)
