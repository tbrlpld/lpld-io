"""
Django settings for lpld project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url  # type: ignore
import dotenv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    host.strip() for host in os.environ.get("ALLOWED_HOSTS", "").split(",") if host
]

if DEBUG:
    # The internal ips settings is needed to activate the debug toolbar.
    INTERNAL_IPS = [
        ip.strip() for ip in os.environ.get("INTERNAL_IPS", "").split(",") if ip
    ]


# Application definition

INSTALLED_APPS = [
    "lpld.core",
    "lpld.home",
    "lpld.images",
    "lpld.mediafiles",
    "lpld.projects",
    "lpld.utils",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.search_promotions",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "heroicons",
    "modelcluster",
    "slippers",
    "taggit",
    "wagtailmedia",
    "widget_tweaks",
]

if DEBUG:
    INSTALLED_APPS.extend(
        [
            "lpld.templatetag_overrides",
            "wagtail.contrib.styleguide",
            "debug_toolbar",
            "pattern_library",
        ]
    )

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

if DEBUG:
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "lpld.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path(BASE_DIR).joinpath("lpld/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "lpldutils": "lpld.templatetags.lpldutils",
            },
        },
    },
]

if DEBUG:
    TEMPLATES[0]["OPTIONS"]["builtins"] = [  # type: ignore
        "pattern_library.loader_tags",
    ]
    PATTERN_LIBRARY = {
        # Groups of templates for the pattern library navigation. The keys
        # are the group titles and the values are lists of template name
        # prefixes that will be searched to populate the groups.
        "SECTIONS": (
            ("atoms", ["atoms"]),
            ("molecules", ["molecules"]),
            ("organisms", ["organisms"]),
            ("pages", ["pages"]),
            ("design", ["design-system"]),
        ),
        # Configure which files to detect as templates.
        "TEMPLATE_SUFFIX": ".html",
        # Set which template components should be rendered inside of,
        # so they may use page-level component dependencies like CSS.
        "PATTERN_BASE_TEMPLATE_NAME": "base.html",
        # Any template in BASE_TEMPLATE_NAMES or any template that
        # extends a template in BASE_TEMPLATE_NAMES is a "page" and will be
        # rendered as-is without being wrapped.
        "BASE_TEMPLATE_NAMES": ["base-page.html"],
    }

WSGI_APPLICATION = "lpld.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# https://github.com/jacobian/dj-database-url


DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "sqlite:///" + str(Path(BASE_DIR).joinpath("db.sqlite3")),
)
DATABASES = {}
DATABASES["default"] = dj_database_url.parse(DATABASE_URL)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGIN_REDIRECT_URL = "home:home"
LOGOUT_REDIRECT_URL = "home:home"

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [
    BASE_DIR / "lpld/static/comp",
    BASE_DIR / "lpld/static/public",
]
STATIC_ROOT = BASE_DIR / "lpld/static/dist"
STATIC_URL = "static/"


# Media files (user uploaded content)
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "media/"
# AWS S3 buckets configuration
# This is media files storage backend configuration. S3 is our preferred file
# storage solution.
# To enable this storage backend we use django-storages package...
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
# ...that uses AWS' boto3 library.
# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
#
# Three required environment variables are:
#  * AWS_STORAGE_BUCKET_NAME
#  * AWS_ACCESS_KEY_ID
#  * AWS_SECRET_ACCESS_KEY
# The last two are picked up by boto3:
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#environment-variables
if "AWS_STORAGE_BUCKET_NAME" in os.environ:
    INSTALLED_APPS = INSTALLED_APPS + [
        "storages",
        # "wagtail_storages",
    ]

    # https://docs.djangoproject.com/en/stable/ref/settings/#default-file-storage
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]

    # Disables signing of the S3 objects' URLs. When set to True it
    # will append authorization querystring to each URL.
    AWS_QUERYSTRING_AUTH = False

    # Do not allow overriding files on S3 as per Wagtail docs recommendation:
    # https://docs.wagtail.io/en/stable/advanced_topics/deploying.html#cloud-storage
    # Not having this setting may have consequences in losing files.
    AWS_S3_FILE_OVERWRITE = False

    # Default ACL for new files should be "private" - not accessible to the
    # public. Images should be made available to public via the bucket policy,
    # where the documents should use wagtail-storages.
    # ***
    # I have removed Wagtail storages for now, because it is not compatible with
    # Django 4.0. The CDN features are not really for me anyhow. It seems overkill
    # to combine the S3 and a CDN. I guess the nice thing it adds is that is uses
    # per-object-ACL that correspond to that is defined in Wagtail. Meaning that
    # it uses redirects to signed URLs for private documents.
    # I don't think that I will need this for my personal project. I guess this might
    # be interesting for intranets or something... but that is not what I am building.
    AWS_DEFAULT_ACL = "public-read"

    # We generally use this setting in the production to put the S3 bucket
    # behind a CDN using a custom domain, e.g. media.llamasavers.com.
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
    if "AWS_S3_CUSTOM_DOMAIN" in os.environ:
        AWS_S3_CUSTOM_DOMAIN = os.environ["AWS_S3_CUSTOM_DOMAIN"]

    # When signing URLs is facilitated, the region must be set, because the
    # global S3 endpoint does not seem to support that. Set this only if
    # necessary.
    if "AWS_S3_REGION_NAME" in os.environ:
        AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION_NAME"]

    # This settings lets you force using http or https protocol when generating
    # the URLs to the files. Set https as default.
    # https://github.com/jschneier/django-storages/blob/10d1929de5e0318dbd63d715db4bebc9a42257b5/storages/backends/s3boto3.py#L217
    AWS_S3_URL_PROTOCOL = os.environ.get("AWS_S3_URL_PROTOCOL", "https:")

    # Custom S3 URL to use when connecting to S3, including scheme.
    # Overrides AWS_S3_REGION_NAME and AWS_S3_USE_SSL.
    # To avoid AuthorizationQueryParametersError error, AWS_S3_REGION_NAME should also be set.  # noqa: E501
    # See also:
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    if "AWS_S3_ENDPOINT_URL" in os.environ:
        AWS_S3_ENDPOINT_URL = os.environ["AWS_S3_ENDPOINT_URL"]


# SECURITY

BASIC_AUTH_LOGIN = os.environ.get("BASIC_AUTH_LOGIN")
BASIC_AUTH_PASSWORD = os.environ.get("BASIC_AUTH_PASSWORD")
if BASIC_AUTH_LOGIN and BASIC_AUTH_PASSWORD:
    MIDDLEWARE = ["baipw.middleware.BasicAuthIPWhitelistMiddleware"] + MIDDLEWARE

if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    # This should already happen at the DNS and host level, but to be sure.
    # https://docs.djangoproject.com/en/4.0/ref/settings/#secure-ssl-redirect
    SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "False") == "True"
    if SECURE_SSL_REDIRECT:
        # When running the app behind a proxy (e.g. on Heroku) then the app server
        # won't see the if the request came with SSL. But, usually proxies add that
        # information to a request header. This setting defines that.
        # https://devcenter.heroku.com/articles/http-routing#heroku-headers
        # https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER
        SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # This tell browsers to only try SSL for some number of seconds (if it's long
    # and SSL is not available, they won't be able to reach you... for that time).
    # https://docs.djangoproject.com/en/4.0/ref/settings/#secure-hsts-seconds
    SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", 0))

SILENCED_SYSTEM_CHECKS = [
    # SECURE_HSTS_INCLUDE_SUBDOMAINS. Not using that, because there might be other
    # sites on subdomains for which I don't want HSTS.
    # https://docs.djangoproject.com/en/4.0/ref/settings/#secure-hsts-include-subdomains
    "security.W005",
    # SECURE_HSTS_PRELOAD. Not using this because it's not official.
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security#preloading_strict_transport_security
    # https://docs.djangoproject.com/en/4.0/ref/settings/#secure-hsts-preload
    "security.W021",
]


# WAGTAIL

WAGTAIL_SITE_NAME = "lpld.io"

WAGTAIL_SEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

WAGTAIL_ENABLE_UPDATE_CHECK = False

WAGTAILIMAGES_IMAGE_MODEL = "images.CustomImage"

WAGTAILMEDIA = {
    "MEDIA_MODEL": "mediafiles.CustomMedia",
}


# DEBUG TOOLBAR


def show_toolbar(request):
    """Don't debug toolbar in pattern library."""
    if "pattern-library" in request.path:
        return False
    if "lpld-admin" in request.path:
        return False
    return True


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": "lpld.settings.show_toolbar"}


# MONITORING

SENTRY_DSN = os.environ.get("SENTRY_DSN")
SENTRY_TEST = os.environ.get("SENTRY_TEST", "False").lower() == "true"

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=float(os.environ.get("SENTRY_SAMPLE_RATE", "1.0")),
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        # Define Sentry environment
        environment=os.environ.get("SENTRY_ENVIRONMENT", "development"),
        # Define release version
        release=os.environ.get("HEROKU_RELEASE_VERSION", ""),
    )
