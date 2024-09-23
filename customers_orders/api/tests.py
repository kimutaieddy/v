# api/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Customer, Order

class APITestCase(TestCase):
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Set up a test client
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        # Create a test customer
        self.customer = Customer.objects.create(name="John Doe", code="JD123")
    
    def test_create_customer(self):
        # Test customer creation
        response = self.client.post('/api/customers/', {"name": "Jane Smith", "code": "JS456"})
        self.assertEqual(response.status_code, 201)
    
    def test_create_order(self):
        # Test order creation
        response = self.client.post('/api/orders/', {
            "item": "Test Item",
            "amount": 100.00,
            "customer": self.customer.id,
        })
        self.assertEqual(response.status_code, 201)
    
    def test_list_customers(self):
        # Test listing customers
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, 200)

    def test_list_orders(self):
        # Test listing orders
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
