# from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from hostel_management_api import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('hostel/', include('client.urls')),
    path('src/', include('src_dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
