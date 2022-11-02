from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/page_lock/', include('garpix_admin_lock.urls')),
]
