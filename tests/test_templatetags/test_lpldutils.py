from lpld.templatetags import lpldutils


def test_sentry_meta_return_type():
    """
    Test that the sentry_meta tag returns a string.

    I have no idea of how to test that the tag actually returns the correct string.
    It works when checking manually in the template, but I have not been able to get the
    tag to render something meaningful in a test. I have even tried to create a fake
    view in the test that renders the tag and hit the view with a request, but that
    does not work either.

    So simple test that the tag returns a string it is.

    """
    assert isinstance(lpldutils.sentry_meta(), str)
