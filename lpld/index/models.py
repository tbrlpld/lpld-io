from typing import Any

from lpld.core import models as core_models


class IndexPage(core_models.BasePage):
    template = "pages/index/index-page.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = ["articles.ArticlePage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["index_entries"] = self.get_index_entries()
        return context

    def get_index_entries(self) -> tuple[dict[str, Any], ...]:
        index_entries = []
        for child in self.get_children().live().public():
            index_entries.append(
                {
                    "title": child.title,
                    "url": child.get_url(),
                }
            )
        return tuple(index_entries)
