from django.views import generic

from skills_factory.educations import models


class CategoryListView(generic.ListView):
    model = models.Category
    template_name = "educations/category_list.html"


class CategoryDetailView(generic.DetailView):
    model = models.Category
    template_name = "educations/category_detail.html"


class CourceListView(generic.ListView):
    model = models.Cource
    template_name = "educations/cource_list.html"


class CourceDetailView(generic.DetailView):
    model = models.Cource
    template_name = "educations/cource_detail.html"


class LessonListView(generic.ListView):
    model = models.Lesson
    template_name = "educations/lesson_list.html"


class LessonDetailView(generic.DetailView):
    model = models.Lesson
    template_name = "educations/lesson_detail.html"


class VideoListView(generic.ListView):
    model = models.Video
    template_name = "educations/video_list.html"


class VideoDetailView(generic.DetailView):
    model = models.Video
    template_name = "educations/video_detail.html"


class AnswerCreateView(generic.CreateView):
    model = models.Answer
    fields = ["question", "variant", "written"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        print(self.request.POST.keys())
        return self.request.META.get("HTTP_REFERER")


# Sitemap views
