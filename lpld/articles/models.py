from django.db import models
from wagtail import fields as wagtail_fields
from wagtail.admin import panels
from wagtailmarkdown import blocks as wagtailmarkdown_blocks

from lpld.core import models as core_models


# Create your models here.
class ArticlePage(core_models.BasePage):
    template = "pages/article/article-page.html"
    parent_page_types = ["home.HomePage", "index.IndexPage"]
    subpage_types = []

    introduction = wagtail_fields.RichTextField(max_length=500, null=False, blank=True)
    body = wagtail_fields.StreamField(
        block_types=[
            (
                "markdown",
                wagtailmarkdown_blocks.MarkdownBlock(
                    template="organisms/prose/prose-markdown-block.html",
                )
            ),
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = core_models.BasePage.content_panels + [
        panels.FieldPanel("introduction"),
        panels.FieldPanel("body"),
    ]
