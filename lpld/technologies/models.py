from django.db import models

from wagtail.admin import panels
from wagtail.snippets import models as snippet_models


@snippet_models.register_snippet
class Technology(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    panels = [
        panels.FieldPanel("name"),
    ]

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name
