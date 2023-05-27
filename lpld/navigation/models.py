from django.db import models

from modelcluster import models as cluster_models
from wagtail import models as wagtail_models
from wagtail.admin import panels
from wagtail.contrib.settings import models as settings_models

from lpld.core import models as core_models


@settings_models.register_setting
class PrimaryNavigationSetting(
    cluster_models.ClusterableModel,
    settings_models.BaseSiteSetting,
):
    panels = [
        panels.InlinePanel("links", label="Link"),
    ]


class PrimaryNavigationLink(wagtail_models.Orderable, core_models.AbstractLink):
    primary_navigation = cluster_models.ParentalKey(
        PrimaryNavigationSetting,
        null=False,
        blank=False,
        related_name="links",
        on_delete=models.CASCADE,
    )
