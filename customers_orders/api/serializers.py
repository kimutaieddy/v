from rest_framework import serializers
from .models import Customer, Order 

class CustomerSerializer(serializers.modelsserializers):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code' , 'created_at', 'updated_at']