from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import store.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("accounts.urls")),
    path("", include(store.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
