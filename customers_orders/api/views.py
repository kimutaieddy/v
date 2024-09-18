from  .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets
from  rest_framework import authentication, permissions 

#ViewSets define the view behavior for the API views customers
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.filter(...)  # Add custom filtering logic here

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer      