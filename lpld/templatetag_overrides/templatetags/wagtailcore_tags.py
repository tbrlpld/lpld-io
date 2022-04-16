from pattern_library.monkey_utils import override_tag  # type: ignore
from wagtail.core.templatetags.wagtailcore_tags import register

override_tag(register, name="pageurl", default_html="https://example.com")
override_tag(register, name="include_block")
