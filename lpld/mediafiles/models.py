from wagtailmedia import models as media_models


class CustomMedia(media_models.AbstractMedia):
    admin_form_fields = media_models.Media.admin_form_fields
