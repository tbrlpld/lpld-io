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
