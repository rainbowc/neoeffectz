
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from neoeffects.sitemaps import StaticViewSitemap


sitemaps_dict = {"static": StaticViewSitemap()}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("neoeffects.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="django.contrib.sitemaps.views.sitemap"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^robots\.txt$', serve, {'document_root': settings.STATIC_ROOT, 'path': "robots.txt"}),
]