from pattern_library.monkey_utils import override_tag  # type: ignore
from lpld.templatetags.navigation import register

override_tag(register, name="primary_navigation", default_html="Primary Navigation")
