from django.db import models
import uuid

class Customer(models.Model):
    name = models.CharField(max_length=255)
    code = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'code']),
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"

class Order(models.Model):
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order: {self.item}, Amount: {self.amount} for {self.customer.name}"
