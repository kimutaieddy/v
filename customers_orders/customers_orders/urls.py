from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


#cudtomize routers

router=DefaultRouter()       
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)


urlpatterns = [
    path('',include('router.urls')),
]
