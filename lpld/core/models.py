from django.db import models
from django.utils import functional as func_utils

from modelcluster import models as cluster_models
from wagtail import models as wagtail_models
from wagtail.admin import panels
from wagtail.contrib.settings import models as settings_models


from lpld.core import settings as settings_utils


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

    def get_context(self, request):
        context = super().get_context(request)
        context["primary_navigation_links"] = (
            settings_utils.get_primary_navigation_links(request)
        )
        return context


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
    def url(self):
        return self.page.get_url()

    class Meta:
        abstract = True


@settings_models.register_setting
class PrimaryNavigationSetting(
    cluster_models.ClusterableModel,
    settings_models.BaseSiteSetting,
):
    panels = [
        panels.InlinePanel("links", label="Link"),
    ]


class PrimaryNavigationLink(wagtail_models.Orderable, AbstractLink):
    primary_navigation = cluster_models.ParentalKey(
        PrimaryNavigationSetting,
        null=False,
        blank=False,
        related_name="links",
        on_delete=models.CASCADE,
    )
