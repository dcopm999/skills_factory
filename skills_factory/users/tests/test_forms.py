from django.test import TestCase

from skills_factory.users.forms import UserCreationForm
from skills_factory.users.tests.factories import UserFactory


class UserTestCase(TestCase):
    def test_create_user_form(self):
        factory = UserFactory()
        data = {
            "first_name": factory.first_name,
            "last_name": factory.last_name,
            "username": factory.username,
            "password1": factory.password,
            "password2": factory.password,
            "image": factory.image,
            "email": factory.email,
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_username(), factory.username)
        form.save()
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue("username" in form.errors)
