from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from skills_factory.educations import views_api as educations_views
from skills_factory.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("category", educations_views.CategoryViewSet)
router.register("cource", educations_views.CourceViewSet)
router.register("lesson", educations_views.LessonViewSet)
router.register("video", educations_views.VideoViewSet)
router.register("book", educations_views.BookViewSet)
router.register("question", educations_views.QuestionViewSet)
router.register("variant", educations_views.VariantViewSet)
router.register("validvariant", educations_views.ValidVariantViewSet)
router.register("answer", educations_views.AnswerViewSet)

app_name = "api"
urlpatterns = router.urls
