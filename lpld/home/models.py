from django.apps import apps
from django.db import models

from wagtail import fields
from wagtail import images as wagtail_images
from wagtail import models as wagtail_models
from wagtail.admin import panels


class HomePage(wagtail_models.Page):
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

    content_panels = wagtail_models.Page.content_panels + [
        panels.FieldPanel("introduction"),
        panels.FieldPanel("profile_image"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        ProjectPage = apps.get_model("projects", "ProjectPage")
        context["projects"] = ProjectPage.objects.all()

        return context
