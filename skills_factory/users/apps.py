from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "skills_factory.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import skills_factory.users.signals  # noqa F401
        except ImportError:
            pass
