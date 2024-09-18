from rest_framework import serializers
from .models import Customer, Order 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code' , 'created_at', 'updated_at']

class OrderSerializer(serializers.modelsserializers):
    Customer = CustomerSerializer(read_only=True) # Nested serializer to show customer details(Like preview in Django Admin(Suggested))
    class Meta:
        model = Order
        fields = ['id', 'item', 'amount', 'time', 'customer']