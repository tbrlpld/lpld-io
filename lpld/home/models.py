from django.apps import apps
from django.db import models
from django.utils import html as html_utils

from wagtail import fields
from wagtail import images as wagtail_images
from wagtail.admin import panels

from lpld.core import models as core_models
from lpld.templates.molecules.teaser import teaser


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

        ProjectPage = apps.get_model("projects", "ProjectPage")
        context["projects"] = ProjectPage.objects.all()

        return context

    def get_meta_description(self):
        return self.search_description or self.get_introduction_without_tags() or ""

    def get_introduction_without_tags(self):
        """Return introduction but without the HTMl tags."""
        return html_utils.strip_tags(self.introduction)

    @property
    def project_teasers(self):
        ProjectPage = apps.get_model("projects", "ProjectPage")

        return [
            teaser.Teaser(
                heading=project_page.title,
                introduction=project_page.introduction,
                href=project_page.get_url(),
                image=project_page.image,
                image_shadow=project_page.image_shadow,
                video=project_page.video,
            )
            for project_page in ProjectPage.objects.live().public()
        ]


