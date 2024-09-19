# Import models and serializers
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets
from rest_framework import authentication, permissions
from django_ratelimit.decorators import ratelimit

# ViewSet for Customer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(is_active=True)
    serializer_class = CustomerSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
       return Customer.objects.filter(is_active=True)

# ViewSet for Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
       return Order.objects.all()

@ratelimit(key="ip",)
