from wagtail.core import blocks as wagtail_blocks
from wagtail.images import blocks as image_blocks


class ActionLinkValue(wagtail_blocks.StructValue):
    @property
    def url(self):
        page = self.get("page")
        if page:
            return page.url

        external_url = self.get("external_url")
        if external_url:
            return external_url

        phone_number = self.get("phone_number")
        if phone_number:
            return f"tel://{ phone_number }"

        email = self.get("email")
        if email:
            return f"email://{ email }"


class ActionLink(wagtail_blocks.StructBlock):
    text = wagtail_blocks.CharBlock(required=True, max_length=50)

    page = wagtail_blocks.PageChooserBlock(required=False)
    external_url = wagtail_blocks.URLBlock(required=False, max_length=250)
    phone_number = wagtail_blocks.CharBlock(required=False, max_length=10)
    email = wagtail_blocks.EmailBlock(required=False)

    class Meta:
        icons = "link"
        value_class = ActionLinkValue


class TeaserLink(wagtail_blocks.StructBlock):
    heading = wagtail_blocks.CharBlock(required=True, max_length=50)
    tagline = wagtail_blocks.CharBlock(required=True, max_length=250)
    page = wagtail_blocks.PageChooserBlock(required=True)

    class Meta:
        template = "atoms/teaser-link/teaser-link-block.html"
        icon = "arrow-right"


class CallToAction(wagtail_blocks.StructBlock):
    supertitle = wagtail_blocks.CharBlock(required=True, max_length=50)
    title = wagtail_blocks.CharBlock(required=True, max_length=50)

    action_links = wagtail_blocks.ListBlock(ActionLink(), min_num=1, max_num=2)

    class Meta:
        template = "molecules/call-to-action/call-to-action-block.html"
        icon = "login"


class CategoryTeaserLinks(wagtail_blocks.StructBlock):
    category = wagtail_blocks.CharBlock(required=False, max_length=50)
    tagline = wagtail_blocks.CharBlock(required=True, max_length=250)
    introduction = wagtail_blocks.TextBlock(required=False, max_length=500)

    category_link_text = wagtail_blocks.CharBlock(required=False, max_length=50)
    category_link_page = wagtail_blocks.PageChooserBlock(required=False)

    teaser_links = wagtail_blocks.ListBlock(TeaserLink)

    class Meta:
        template = "molecules/category-teaser-links/category-teaser-links-block.html"
        icon = "tasks"


class TeaserLinksFeature(wagtail_blocks.StructBlock):
    supertitle = wagtail_blocks.CharBlock(
        required=False,
        max_length=50,
        help_text="Displayed above the title.",
    )
    title = wagtail_blocks.CharBlock(
        required=True,
        max_length=50,
        help_text="Title for the main product or service you want to highlight.",
    )
    subtitle = wagtail_blocks.CharBlock(
        required=False, max_length=150, help_text="Displayed below the title."
    )

    action_link_text = wagtail_blocks.CharBlock(
        required=False,
        max_length=50,
        help_text=(
            "Describe the action you want the user to take. "
            'Avoid generic text like "learn more".'
        ),
    )
    action_link_page = wagtail_blocks.PageChooserBlock(
        required=False,
        help_text="Choose the page on which the user can take the action.",
    )

    teaser_links = wagtail_blocks.ListBlock(TeaserLink)

    class Meta:
        template = "molecules/teaser-links-feature/teaser-links-feature-block.html"
        icon = "arrow-right"


class ImageFeatureWithTeaserLinks(wagtail_blocks.StructBlock):
    supertitle = wagtail_blocks.CharBlock(
        required=False,
        max_length=50,
        help_text="Displayed above the title.",
    )
    title = wagtail_blocks.CharBlock(
        required=True,
        max_length=50,
        help_text="Title for the main product or service you want to highlight.",
    )
    subtitle = wagtail_blocks.CharBlock(
        required=False, max_length=150, help_text="Displayed below the title."
    )

    action_link_text = wagtail_blocks.CharBlock(
        required=False,
        max_length=50,
        help_text=(
            "Describe the action you want the user to take. "
            'Avoid generic text like "learn more".'
        ),
    )
    action_link_page = wagtail_blocks.PageChooserBlock(
        required=False,
        help_text="Choose the page on which the user can take the action.",
    )

    image = image_blocks.ImageChooserBlock(required=True)

    teaser_links = wagtail_blocks.ListBlock(TeaserLink())

    class Meta:
        template = "organisms/image-feature/image-feature-with-teaser-links-block.html"
        icon = "image"


class CustomerLogos(wagtail_blocks.StructBlock):
    heading = wagtail_blocks.CharBlock(required=True, default="Trusted by")

    class Meta:
        template = "molecules/customer-logos/customer-logos-block.html"
        icon = "group"
