import factory

from skills_factory.users import models


class UserFactory(factory.Factory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    image = factory.Faker("image_url")
    password = factory.Faker("password")

    class Meta:
        model = models.User
