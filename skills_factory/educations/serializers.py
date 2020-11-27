from rest_framework import serializers

from skills_factory.educations import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ["slug"]


class CourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cource
        exclude = ["slug"]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        exclude = ["slug"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        exclude = ["slug"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = "__all__"


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variant
        fields = "__all__"


class ValidVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ValidVariant
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = "__all__"
