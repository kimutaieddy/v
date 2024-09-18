from django.db import models

class Customer(models.Model):
    name = models.TextField() 
    code = models.UUIDField(unique=True,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:
        index_together = [['name', 'code']]

    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    def __str__(self):
        return f"{self.item} ({self.amount})"