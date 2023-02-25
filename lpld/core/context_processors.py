from django.conf import settings


def sentry_settings(request):
    return {
        "sentry_settings": {
            "SENTRY_DSN": settings.SENTRY_DSN,
            "SENTRY_SAMPLE_RATE": settings.SENTRY_SAMPLE_RATE,
            "SENTRY_ENVIRONMENT": settings.SENTRY_ENVIRONMENT,
            "SENTRY_TEST": settings.SENTRY_TEST,
            "HEROKU_RELEASE_VERSION": settings.HEROKU_RELEASE_VERSION,
        }
    }
