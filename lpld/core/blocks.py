from wagtail import blocks
from wagtail.admin import panels


class HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)

    panels = [panels.FieldPanel("text", classname="full")]

    class Meta:
        template = "atoms/heading/heading-block.html"
        icon = "title"


class SubheadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)

    panels = [panels.FieldPanel("text")]

    class Meta:
        template = "atoms/heading/subheading-block.html"
        icon = "title"


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
