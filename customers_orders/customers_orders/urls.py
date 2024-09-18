from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('api.urls')),  # Include API routes under /api/
    path('health/', include('health_check.urls'))  # Add health check endpoint
    path('api/', include(('api.urls', 'api'), namespace='api')),  # Include API routes under /api/ with namespace
]
