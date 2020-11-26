from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from slugify import slugify

USER = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(verbose_name=_("Slug"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("educations:category-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Cource(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Category"),
    )
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    desc = models.TextField(verbose_name=_("Description"))
    slug = models.SlugField(verbose_name=_("Slug"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("educations:cource-detail", kwargs={"slug": self.slug})

    def video_count(self):
        return self.lesson_set.aggregate(video_count=models.Sum("video")).get(
            "video_count"
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cource, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Cource")
        verbose_name_plural = _("Cources")


class Lesson(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    cource = models.ForeignKey(
        Cource, on_delete=models.CASCADE, verbose_name=_("Cource name")
    )
    desc = models.TextField(verbose_name=_("Description"))
    slug = models.SlugField(verbose_name=_("Slug"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("educations:lesson-detail", kwargs={"slug": self.slug})

    def video_count(self):
        return self.video_set.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lesson, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")


class Video(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    desc = models.TextField(verbose_name=_("Description"))
    url = models.URLField(unique=True, verbose_name=_("URL for video"))
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name=_("Lesson")
    )
    teacher = models.ForeignKey(
        USER, on_delete=models.CASCADE, verbose_name=_("Teacher")
    )
    slug = models.SlugField(verbose_name=_("Slug"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("educations:video-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Video, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    cource = models.ForeignKey(
        Cource, on_delete=models.CASCADE, verbose_name=_("Cource")
    )
    path = models.FileField(upload_to="books", verbose_name=_("Path"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Question(models.Model):
    text = models.TextField(verbose_name=_("Text"))
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name=_("Lesson")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class Variant(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name=_("Question")
    )
    text = models.TextField(verbose_name=_("Text"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")


class ValidVariant(models.Model):
    question = models.OneToOneField(
        Question, on_delete=models.CASCADE, verbose_name=_("Question")
    )
    variant = models.OneToOneField(
        Variant, on_delete=models.CASCADE, verbose_name=_("Answer")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.variant.text

    class Meta:
        verbose_name = _("Valid variant")
        verbose_name_plural = _("Valid Variants")


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name=_("Question")
    )
    user = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name=_("User"))
    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Variant response"),
    )
    written = models.CharField(
        max_length=250, blank=True, verbose_name=_("Written response")
    )
    is_valid = models.NullBooleanField(verbose_name=_("Valid"))

    def __str__(self):
        return str(self.is_valid)

    def answer_validator(self):
        if self.variant is not None:
            if self.question.validvariant.variant == self.variant:
                result = True
            else:
                result = False
        else:
            result = None
        return result

    def save(self, *args, **kwargs):
        self.is_valid = self.answer_validator()
        super(Answer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
