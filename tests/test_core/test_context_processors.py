from lpld.core import context_processors


def test_plausible_settings(settings, rf):
    PLAUSIBLE_DOMAIN: str = "example.com"
    settings.PLAUSIBLE_DOMAIN = PLAUSIBLE_DOMAIN
    request = rf.get("/")

    context = context_processors.plausible_settings(request)

    assert context == {
        "plausible_settings": {
            "PLAUSIBLE_DOMAIN": PLAUSIBLE_DOMAIN,
        },
    }


def test_sentry_settings(settings, rf):
    SENTRY_DSN: str = "https://example.com"
    SENTRY_SAMPLE_RATE: float = 1.0
    SENTRY_ENVIRONMENT: str = "test"
    SENTRY_TEST: bool = True
    HEROKU_RELEASE_VERSION: str = "1"
    settings.SENTRY_DSN = SENTRY_DSN
    settings.SENTRY_SAMPLE_RATE = SENTRY_SAMPLE_RATE
    settings.SENTRY_ENVIRONMENT = SENTRY_ENVIRONMENT
    settings.SENTRY_TEST = SENTRY_TEST
    settings.HEROKU_RELEASE_VERSION = HEROKU_RELEASE_VERSION
    request = rf.get("/")

    context = context_processors.sentry_settings(request)

    assert context == {
        "sentry_settings": {
            "SENTRY_DSN": SENTRY_DSN,
            "SENTRY_SAMPLE_RATE": SENTRY_SAMPLE_RATE,
            "SENTRY_ENVIRONMENT": SENTRY_ENVIRONMENT,
            "SENTRY_TEST": SENTRY_TEST,
            "HEROKU_RELEASE_VERSION": HEROKU_RELEASE_VERSION,
        },
    }
