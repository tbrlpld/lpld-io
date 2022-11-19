from django.db import models

from modelcluster import fields as cluster_fields
from wagtail import fields as wagtail_fields
from wagtail import images as wagtail_images
from wagtail import models as wagtail_models
from wagtail.admin import panels
from wagtailmedia import edit_handlers as media_panels

from lpld.core import models as core_models


class ProjectTechnologyRelation(wagtail_models.Orderable):
    project_page = cluster_fields.ParentalKey(
        "projects.ProjectPage",
        on_delete=models.CASCADE,
        related_name="related_technologies",
    )
    technology = models.ForeignKey(
        "core.Technology",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="related_projects",
    )

    panels = [panels.FieldPanel("technology")]


class ProjectPage(core_models.BasePage):
    parent_page_types = ["home.HomePage"]
    template = "pages/project-page/project-page.html"

    image = models.ForeignKey(
        wagtail_images.get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    video = models.ForeignKey(
        "mediafiles.CustomMedia",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    image_shadow = models.BooleanField(help_text="Add drop shadow to the image?")

    introduction = models.TextField(null=False, blank=True)
    description = wagtail_fields.RichTextField(
        features=["link"],
        null=False,
        blank=True,
    )

    repo_url = models.URLField(null=False, blank=True)
    demo_url = models.URLField(null=False, blank=True)

    content_panels = core_models.BasePage.content_panels + [
        panels.MultiFieldPanel(
            children=[
                panels.FieldPanel("image"),
                media_panels.MediaChooserPanel("video", media_type="video"),
                panels.FieldPanel("image_shadow"),
            ],
            heading="Image",
        ),
        panels.FieldPanel("introduction"),
        panels.FieldPanel("description"),
        panels.MultiFieldPanel(
            children=[
                panels.FieldPanel("repo_url"),
                panels.FieldPanel("demo_url"),
            ],
            heading="Links",
        ),
        panels.InlinePanel(
            "related_technologies", heading="Used technologies", label="Technology"
        ),
    ]
