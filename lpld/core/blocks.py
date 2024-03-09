from wagtail import blocks
from wagtail.admin import panels


class HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)

    panels = [panels.FieldPanel("text", classname="full")]

    class Meta:
        template = "atoms/heading/heading.html"
        icon = "title"

    def get_context(self, value, parent_context=None):
        return {
            "level": 2,
            "size": "md",
            "children": value.get("text"),
        }


class SubheadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)

    panels = [panels.FieldPanel("text")]

    class Meta:
        template = "atoms/heading/heading.html"
        icon = "title"

    def get_context(self, value, parent_context=None):
        return {
            "level": 3,
            "size": "sm",
            "children": value.get("text"),
        }


class PageLinkBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock(required=True)
    text = blocks.CharBlock(
        required=False,
        help_text = "Text for the link. Defaults to page title.",
    )

    class Meta:
        icon = "doc-full"
        template = "atoms/link/link.html"

    def get_context(self, value, parent_context=None):
        page = value.get("page")
        text = value.get("text")
        return {
            "text": text or page.title,
            "href": page.get_url(),
        }


class LinkStream(blocks.StreamBlock):
    """
    Stream of links.

    Each item should return context objects containing the keys `"text"` and `"href"`
    from their `get_context` method.
    """
    page_link = PageLinkBlock()

    class Meta:
        icon = "list-ul"
        template = "molecules/link-listing/link-listing.html"
        min_num = 1

    def get_context(self, value, parent_context=None):
        links = [
            bb.block.get_context(bb.value)
            for bb in value
        ]
        return {"links": links}


class LinkBlock(LinkStream):
    """
    Link stream with max 1 item.

    Can be used as a flexible link block.
    """

    class Meta:
        icon = "link"
        template = "atoms/link/link.html"
        min_num = 1
        max_num = 1

    def get_context(self, value, parent_context=None):
        bound_block = value[0]
        return bound_block.block.get_context(bound_block.value)



class SectionBlock(blocks.StructBlock):
    heading = HeadingBlock()
    body = blocks.StreamBlock(
        local_blocks=[
            ("paragraph", blocks.RichTextBlock(features=["link", "bold", "italics"])),
            # ("paragraph", blocks.RichTextBlock(features=["link", "bold", "italics"])), ]
        ],
        min_num=0,
        required=False,
    )

    panels = [
        panels.FieldPanel("heading"),
        panels.FieldPanel("body"),
    ]

    class Meta:
        template = "molecules/section/section-block.html"
        icon = "bars"
