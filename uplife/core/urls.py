from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

# favicon_view = RedirectView.as_view(
#     url="/static/analysis/assets/images/logo.ico", permanent=True
# )


urlpatterns = [
    path(
        "",
        RedirectView.as_view(url="/api/docs/", permanent=True),
        name="Root",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(  # Optional UI:
        "api/docs/",
        SpectacularSwaggerView.as_view(template_name="swagger/swagger-ui.html", url_name="schema"),
        name="swagger-ui",
    ),
    # path("favicon.ico", favicon_view),
    path("admin/", admin.site.urls),
    path("api/auth/", include("users.urls")),
    path("api/recipients/", include("recipients.urls")),
    path("api/donations/", include("donations.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

