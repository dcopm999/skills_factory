from django.urls import path

from skills_factory.educations import views

app_name = "educations"

urlpatterns = [
    path("cource/list", views.CourceListView.as_view(), name="cource-list"),
    path("cource/<slug:slug>", views.CourceDetailView.as_view(), name="cource-detail"),
    path("lesson/list", views.LessonListView.as_view(), name="lesson-list"),
    path("lesson/<slug:slug>", views.LessonDetailView.as_view(), name="lesson-detail"),
    path("video/list", views.VideoListView.as_view(), name="video-list"),
    path("video/<slug:slug>", views.VideoDetailView.as_view(), name="video-detail"),
    path("answer/", views.AnswerCreateView.as_view(), name="answer-create"),
]
