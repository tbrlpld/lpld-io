from django.db import models
from django.utils import functional as func_utils

from wagtail.admin import panels
from wagtail.core import models as wagtail_models


class BasePage(wagtail_models.Page):
    class Meta(wagtail_models.Page.Meta):
        abstract = True

    @func_utils.cached_property
    def title_tag_content(self):
        return self.get_title_tag_content()

    def get_title_tag_content(self):
        title_text = self.seo_title or self.title
        title_text = f"{ title_text } · lpld.io"
        return title_text

    @func_utils.cached_property
    def meta_description(self):
        return self.get_meta_description

    def get_meta_description(self):
        return self.search_description or ""


# TODO: Once the technologies.Technology model is in production,
#       this model can be deleted.
class Technology(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    panels = [
        panels.FieldPanel("name"),
    ]

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name
