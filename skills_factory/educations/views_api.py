from rest_framework import viewsets

from skills_factory.educations import models, serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CourceViewSet(viewsets.ModelViewSet):
    queryset = models.Cource.objects.all()
    serializer_class = serializers.CourceSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class VariantViewSet(viewsets.ModelViewSet):
    queryset = models.Variant.objects.all()
    serializer_class = serializers.VariantSerializer


class ValidVariantViewSet(viewsets.ModelViewSet):
    queryset = models.ValidVariant.objects.all()
    serializer_class = serializers.ValidVariantSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
