from django.urls import path, include  # Import necessary modules for URL routing
from rest_framework.routers import SimpleRouter  # Import SimpleRouter for API routing
from .views import CustomerViewSet, OrderViewSet  # Import CustomerViewSet and OrderViewSet from views module
# Initialize SimpleRouter instance
router = SimpleRouter()
router.register(r'customers', CustomerViewSet)  # Register CustomerViewSet with router
router.register(r'orders', OrderViewSet)  # Register OrderViewSet with router

urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
]