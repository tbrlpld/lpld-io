from django.contrib import auth
from django.core import management


class Command(management.base.BaseCommand):
    def handle(self, *args, **kwargs):
        User = auth.get_user_model()
        User.objects.create_superuser(
            username="admin", email="admin@example.com", password="admin"
        )
        self.stdout.write("Done.")
