from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from sorl.thumbnail.admin import AdminImageMixin

from skills_factory.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(AdminImageMixin, auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("image",)}),) + tuple(
        auth_admin.UserAdmin.fieldsets
    )
    list_display = ["username", "is_superuser"]
    search_fields = ["username"]
