import datetime

import factory

from skills_factory.educations import models
from skills_factory.users.tests.factories import UserFactory


class CourceFactory(factory.django.DjangoModelFactory):
    name = "Math"
    title = "Title for math"
    desc = "Descrtiption for Math"
    created = factory.LazyFunction(datetime.datetime.now)
    updated = factory.LazyFunction(datetime.datetime.now)

    class Meta:
        model = models.Cource


class LessonFactory(factory.django.DjangoModelFactory):
    name = "Lesson 1"
    cource = CourceFactory()
    title = "Lesson title"
    desc = "Description of lesson"
    created = factory.LazyFunction(datetime.datetime.now)
    updated = factory.LazyFunction(datetime.datetime.now)

    class Meta:
        model = models.Lesson


class VideoFactory(factory.django.DjangoModelFactory):
    name = "Video name"
    title = "Video title"
    desc = "Video description"
    lesson = LessonFactory()
    teacher = UserFactory.create()
    created = factory.LazyFunction(datetime.datetime.now)
    updated = factory.LazyFunction(datetime.datetime.now)

    class Meta:
        model = models.Video
