from wagtail import fields as wagtail_fields
from wagtail.admin import panels
from wagtailmarkdown import blocks as wagtailmarkdown_blocks

from lpld.core import models as core_models

class BlogIndexPage(core_models.BasePage):
    template = "pages/blog/blog-index-page.html"
    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogPage']


class BlogPage(core_models.BasePage):
    template = "pages/blog/blog-page.html"
    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    body = wagtail_fields.StreamField(
        block_types=[('markdown', wagtailmarkdown_blocks.MarkdownBlock())],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = core_models.BasePage.content_panels + [
        panels.FieldPanel('body'),
    ]
