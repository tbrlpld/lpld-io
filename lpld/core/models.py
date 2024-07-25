from django.db import models
from django.utils import functional as func_utils

from wagtail import models as wagtail_models
from wagtail.admin import panels

from lpld.navigation import utils as nav_utils


class BasePage(wagtail_models.Page):
    class Meta(wagtail_models.Page.Meta):
        abstract = True

    @func_utils.cached_property
    def title_tag_content(self):
        return self.get_title_tag_content()

    def get_title_tag_content(self) -> str:
        parts = self.get_title_tag_parts()
        sep = self.get_title_separator()
        return sep.join(parts)

    def get_title_tag_parts(self) -> list[str]:
        title = self.seo_title or self.title
        last = self.get_title_tag_last_part()
        return [title, last]

    def get_title_tag_last_part(self) -> str:
        """Return the last part for the title tag."""
        return "lpld.io"

    def get_title_separator(self) -> str:
        return " · "

    @func_utils.cached_property
    def meta_description(self):
        return self.get_meta_description

    def get_meta_description(self):
        return self.search_description or ""


class AbstractLink(models.Model):
    page = models.ForeignKey(
        "wagtailcore.Page",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    text_override = models.CharField(
        max_length=65,
        null=False,
        blank=True,
    )

    panels = [
        panels.FieldPanel("text_override", heading="Text"),
        panels.FieldPanel("page"),
    ]

    @property
    def text(self):
        return self.text_override or self.page.title

    @property
    def href(self):
        return self.page.get_url()

    class Meta:
        abstract = True
