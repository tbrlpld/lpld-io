from django import shortcuts
from django.views import defaults
from django.views.generic import base as generic_views


class RobotsView(generic_views.TemplateView):
    template_name = "pages/robots.txt"


def handle_400(request, exception=None):
    return defaults.bad_request(
        request,
        exception,
        template_name="pages/errors/400.html"
    )


def handle_403(request, exception=None):
    return defaults.permission_denied(
        request,
        exception,
        template_name="pages/errors/403.html"
    )


def handle_404(request, exception=None):
    return defaults.page_not_found(
        request,
        exception,
        template_name="pages/errors/404.html"
    )


def handle_500(request):
    return defaults.server_error(
        request,
        template_name="pages/errors/500.html"
    )


def error_test_view(request, error_code):
    error_views = {
        400: handle_400,
        403: handle_403,
        404: handle_404,
        500: handle_500,
    }
    return error_views[error_code](request)
