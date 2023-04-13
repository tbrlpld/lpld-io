from django.db import models
from wagtail import fields as wagtail_fields
from wagtail.admin import panels
from wagtailmarkdown import blocks as wagtailmarkdown_blocks

from lpld.core import models as core_models


class BlogIndexPage(core_models.BasePage):
    template = "pages/blog/blog-index-page.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.BlogPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["index_entries"] = self.get_index_entries()
        return context

    def get_index_entries(self) -> tuple[dict[str, str]]:
        index_entries = []
        for child in self.get_children().only("title"):
            index_entries.append(
                {
                    "title": child.title,
                    "url": child.get_url(),
                }
            )
        return tuple(index_entries)


class BlogPage(core_models.BasePage):
    template = "pages/blog/blog-page.html"
    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []

    introduction = models.TextField(max_length=500, null=False, blank=True)
    body = wagtail_fields.StreamField(
        block_types=[
            ("markdown", wagtailmarkdown_blocks.MarkdownBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = core_models.BasePage.content_panels + [
        panels.FieldPanel("introduction"),
        panels.FieldPanel("body"),
    ]
