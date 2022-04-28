from django.apps import apps

from wagtail.admin import edit_handlers
from wagtail.core import fields
from wagtail.core import models as wagtail_models


class HomePage(wagtail_models.Page):
    """docstring for HomePage"""

    max_count = 1
    template = "pages/home/home.html"

    introduction = fields.RichTextField(features=["link"], null=True, blank=True)

    content_panels = wagtail_models.Page.content_panels + [
        edit_handlers.FieldPanel("introduction"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        ProjectPage = apps.get_model("projects", "ProjectPage")
        context["projects"] = ProjectPage.objects.all()

        return context
