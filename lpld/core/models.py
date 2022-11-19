from django.db import models
from django.utils import functional

from wagtail.core import models as wagtail_models
from wagtail.admin import panels
from wagtail.snippets import models as snippet_models


class BasePage(wagtail_models.Page):
    class Meta(wagtail_models.Page.Meta):
        abstract = True

    @functional.cached_property
    def meta_description(self):
        return self.get_meta_description

    def get_meta_description(self):
        return self.search_description or ""


@snippet_models.register_snippet
class Technology(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    panels = [
        panels.FieldPanel("name"),
    ]

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name
