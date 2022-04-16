from django.db import models

from wagtail.admin import edit_handlers
from wagtail.core import fields
from wagtail.core import models as wagtail_models
from wagtail.images import edit_handlers as image_handlers

from lpld.core import blocks


class HomePage(wagtail_models.Page):
    """docstring for HomePage"""

    template = "pages/home/home.html"
