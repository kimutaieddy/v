from django.shortcuts import render
from  .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets

#ViewSets define the view behavior for the API views customers
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
