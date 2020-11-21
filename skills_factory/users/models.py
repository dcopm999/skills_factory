from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField


class User(AbstractUser):
    """Default user for Skills Factory."""

    image = ImageField(
        upload_to="user-images", blank=True, null=True, verbose_name=_("User image")
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
