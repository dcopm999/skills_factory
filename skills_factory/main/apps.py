from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainConfig(AppConfig):
    name = "skills_factory.main"
    verbose_name = _("Main")
