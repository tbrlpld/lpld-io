from django import shortcuts
from django.views.generic import base as generic_views


class RobotsView(generic_views.TemplateView):
    template_name = "pages/robots.txt"


def handle_400(request, exception=None):
    return shortcuts.render(request, template_name="pages/errors/400.html", status=400)


def handle_403(request, exception=None):
    return shortcuts.render(request, template_name="pages/errors/403.html", status=403)


def handle_404(request, exception=None):
    return shortcuts.render(request, template_name="pages/errors/404.html", status=404)


def handle_500(request):
    return shortcuts.render(request, template_name="pages/errors/500.html", status=500)


def error_test_view(request, error_code):
    error_views = {
        400: handle_400,
        403: handle_403,
        404: handle_404,
        500: handle_500,
    }
    return error_views[error_code](request)
