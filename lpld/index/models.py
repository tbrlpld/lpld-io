from typing import Any

from wagtail import fields as wagtail_fields
from wagtail.admin import panels

from lpld.core import models as core_models


class IndexPage(core_models.BasePage):
    template = "pages/index/index-page.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = ["articles.ArticlePage", "projects.ProjectPage"]

    introduction = wagtail_fields.RichTextField(max_length=500, null=False, blank=True)

    content_panels = tuple(core_models.BasePage.content_panels) + (
        panels.FieldPanel("introduction"),
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["index_entries"] = self.get_index_entries()
        return context

    def get_index_entries(self) -> tuple[dict[str, Any], ...]:
        index_entries = []
        for child in self.get_children().live().public():
            index_entries.append(
                {
                    "text": child.title,
                    "href": child.get_url(),
                }
            )
        return tuple(index_entries)
