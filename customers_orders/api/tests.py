from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token  # Import token model
from django.contrib.auth.models import User
from .models import Customer

class APITestCase(TestCase):
    
    def setUp(self):
      
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        
        self.token = Token.objects.create(user=self.user)
        
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        
        self.customer = Customer.objects.create(name="John Doe", code="JD123")
    
def test_create_customer(self):
    response = self.client.post('/api/v1/customers/', {"name": "Jane Smith", "code": "JS456"}, format='json')
    self.assertEqual(response.status_code, 201)

def test_create_order(self):
    response = self.client.post('/api/v1/orders/', {
        "item": "Test Item",
        "amount": 100.00,
        "customer": self.customer.id,
    }, format='json')
    self.assertEqual(response.status_code, 201)

def test_list_customers(self):
    response = self.client.get('/api/v1/customers/')
    self.assertEqual(response.status_code, 200)

def test_list_orders(self):
    response = self.client.get('/api/v1/orders/')
    self.assertEqual(response.status_code, 200)
