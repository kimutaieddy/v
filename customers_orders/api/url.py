
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# Cstom router & reg ur viewsets ..

router=DefaultRouter()       
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)

# Include the router urls in urlpatterns (automatically generates urls for viewsets) 
urlpatterns = [
    path('',include('router.urls')),
]
