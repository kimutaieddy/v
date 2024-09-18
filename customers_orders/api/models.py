from django.db import models
import uuid

class Customer(models.Model):
    name = models.CharField(max_length=255)  # CharField is better for names
    code = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)  # UUIDField with default generator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'code']),  # Preferred over index_together
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"  # Improved for better display

class Order(models.Model):
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order: {self.item}, Amount: {self.amount} for {self.customer.name}"  # More descriptive
