from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('bingapp.urls')),  # Include your app's URL patterns
    path('admin/', admin.site.urls),  # URL pattern for the admin site
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)