from pattern_library.monkey_utils import override_tag  # type: ignore
from wagtail.images.templatetags.wagtailimages_tags import register

override_tag(register, name="image", default_html="IMAGE")
override_tag(register, name="image_url", default_html="IMAGE_URL")
