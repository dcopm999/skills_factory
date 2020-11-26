from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from skills_factory.educations import views
from skills_factory.main import views as main_views

sitemaps = {
    "cource": views.CourceSitemapView,
    "lesson": views.LessonSitemapView,
    "video": views.VideoSitemapView,
}

urlpatterns = [
    path("", main_views.HomeView.as_view(), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("skills_factory.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("educations/", include("educations.urls", namespace="educations")),
    # Your stuff: custom urls includes go here
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

domain_verify = [
    path(
        "google3c2570b4c41d746c.html",
        TemplateView.as_view(template_name="google3c2570b4c41d746c.html"),
    ),
    path(
        "receiver.html",
        TemplateView.as_view(template_name="receiver.html"),
    ),
    path(
        "yandex_cfc6a1a60b4cf69a.html",
        TemplateView.as_view(template_name="yandex_cfc6a1a60b4cf69a.html"),
    ),
]
urlpatterns += domain_verify

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
