from django import shortcuts
from django.views.generic import base as generic_views


class RobotsView(generic_views.TemplateView):
    template_name = "pages/robots.txt"


def handle_404(request, exception):
    return shortcuts.render(request, template_name="pages/errors/404.html", status=404)


def error_test_view(request, error_code):
    error_views = {
        404: handle_404,
    }
    return error_views[error_code](request, exception=None)

