import typing

from lpld.core import context_processors

if typing.TYPE_CHECKING:
    from django import conf, http, test


def test_plausible_settings(
    settings: conf.LazySettings,
    rf: test.RequestFactory,
) -> None:
    plausible_domain: str = "example.com"
    settings.PLAUSIBLE_DOMAIN = plausible_domain
    request: http.HttpRequest = rf.get("/")

    context: dict = context_processors.plausible_settings(request)

    assert context == {
        "plausible_settings": {
            "PLAUSIBLE_DOMAIN": plausible_domain,
        },
    }


def test_sentry_settings(
    settings: conf.LazySettings,
    rf: test.RequestFactory,
) -> None:
    sentry_dsn: str = "https://example.com"
    sentry_sample_rate: float = 1.0
    sentry_environment: str = "test"
    sentry_test: bool = True
    heroku_release_version: str = "1"
    settings.SENTRY_DSN = sentry_dsn
    settings.SENTRY_SAMPLE_RATE = sentry_sample_rate
    settings.SENTRY_ENVIRONMENT = sentry_environment
    settings.SENTRY_TEST = sentry_test
    settings.HEROKU_RELEASE_VERSION = heroku_release_version
    request: http.HttpRequest = rf.get("/")

    context: dict = context_processors.sentry_settings(request)

    assert context == {
        "sentry_settings": {
            "SENTRY_DSN": sentry_dsn,
            "SENTRY_SAMPLE_RATE": sentry_sample_rate,
            "SENTRY_ENVIRONMENT": sentry_environment,
            "SENTRY_TEST": sentry_test,
            "HEROKU_RELEASE_VERSION": heroku_release_version,
        },
    }
