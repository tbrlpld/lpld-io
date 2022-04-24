from django.db import models

from wagtail.images import models as image_models


class CustomImage(image_models.AbstractImage):

    admin_form_fields = image_models.Image.admin_form_fields


class CustomRendition(image_models.AbstractRendition):
    image = models.ForeignKey(
        "images.CustomImage",
        on_delete=models.CASCADE,
        related_name="renditions",
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
