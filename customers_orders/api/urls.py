from django.urls import path, include  
from rest_framework.routers import SimpleRouter  
from .views import CustomerViewSet, OrderViewSet  


# Initialize SimpleRouter instance
router = SimpleRouter()
router.register(r'customers', CustomerViewSet)  
router.register(r'orders', OrderViewSet)  

urlpatterns = [
    path('', include(router.urls)),  
    path('health/', include('health_check.urls')),  # Add health check endpoint
]