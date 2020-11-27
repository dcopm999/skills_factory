from django.contrib import admin

from skills_factory.educations import models


class VariantInline(admin.TabularInline):
    model = models.Variant


class ValidVariantInline(admin.TabularInline):
    model = models.ValidVariant


class LessonInline(admin.TabularInline):
    model = models.Lesson


class VideoInline(admin.StackedInline):
    model = models.Video


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Cource)
class CourceAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["name", "cource"]
    search_fields = ["name", "cource"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Video)
class VideAdmin(admin.ModelAdmin):
    list_display = ["name", "lesson", "title", "url", "teacher"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "cource", "path"]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [VariantInline, ValidVariantInline]
    list_display = ["lesson", "text"]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["user", "question", "variant", "written", "is_valid"]
