from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets, authentication, permissions
from .sms_service import send_sms
from rest_framework.response import Response
from rest_framework.decorators import api_view

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

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()

      
        customer = order.customer
        phone_number = customer.phone_number

        if phone_number:
           
            send_sms(phone_number, f"Hi {customer.name}, your order for {order.item} has been received!")
            return Response(serializer.data, status=201)
        else:
            return Response({"error": "Customer phone number is missing"}, status=400)

    return Response(serializer.errors, status=400)
