from django.conf import settings


def test_not_running_debug():
    assert not settings.DEBUG, "Tests should not run in debug mode."
