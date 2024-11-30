from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('ggfhfhchv/', admin.site.urls),
    # Include the paragraph_generator URLs
    path('', include('paragraph_generator.urls')),  # This will handle all routes from the root URL
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)