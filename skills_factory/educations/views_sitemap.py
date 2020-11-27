from django.contrib.sitemaps import Sitemap

from skills_factory.educations import models


class CourceSitemapView(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return models.Cource.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.get_absolute_url()


class LessonSitemapView(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return models.Lesson.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.get_absolute_url()


class VideoSitemapView(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return models.Video.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.get_absolute_url()


SITEMAPS = {
    "cource": CourceSitemapView,
    "lesson": LessonSitemapView,
    "video": VideoSitemapView,
}
