import dataclasses

from django.db import models
from django.utils import html as html_utils

from wagtail import fields
from wagtail import images as wagtail_images
from wagtail.admin import panels

from lpld.core import models as core_models
from lpld.templates.atoms.heading import heading
from lpld.templates.molecules import section
from lpld.templates.organisms.teaser_grid import teaser_grid


class HomePage(core_models.BasePage):
    """docstring for HomePage"""

    max_count = 1
    template = "pages/home/home.html"

    introduction = fields.RichTextField(features=["link"], null=True, blank=True)
    profile_image = models.ForeignKey(
        wagtail_images.get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    content_panels = core_models.BasePage.content_panels + [
        panels.FieldPanel("introduction"),
        panels.FieldPanel("profile_image"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        extra_context = {
            "title": heading.Heading(text=self.title),
            "introduction": self.introduction,
            "profile_image": self.profile_image,
            "projects": self.get_projects_section(),
        }

        return {**context, **extra_context}

    def get_meta_description(self) -> str:
        return self.search_description or self.get_introduction_without_tags() or ""

    def get_introduction_without_tags(self) -> str:
        """Return introduction but without the HTMl tags."""
        return html_utils.strip_tags(self.introduction)

    def get_projects_section(self) -> section.Section:
        return section.Section(
            html_id="projects",
            html_class="mt-16 lg:mt-32 pt-16 lg:mt-32",
            content=[
                heading.Heading(
                    text="These are things I have build before",
                    level=2,
                    size="md",
                    extra_class="max-w-lg lg:max-w-2xl",
                ),
                teaser_grid.TeaserGrid.from_project_pages()
            ]
        )
