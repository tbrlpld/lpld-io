from django.apps import apps

from wagtail.core import models as wagtail_models


class HomePage(wagtail_models.Page):
    """docstring for HomePage"""

    max_count = 1
    template = "pages/home/home.html"

    def get_context(self, request):
        context = super().get_context(request)

        ProjectPage = apps.get_model("projects", "ProjectPage")
        context["projects"] = ProjectPage.objects.all()

        return context
