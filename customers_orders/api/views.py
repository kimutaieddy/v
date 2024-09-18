from django.shortcuts import render
from  .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets