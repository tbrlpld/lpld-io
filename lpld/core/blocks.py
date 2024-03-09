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

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context.update(
            heading=value.bound_blocks["heading"],
        )
        return context
