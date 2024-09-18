from django.contrib import admin
from .models import Customer, Order

# Register the Customer and Order models so they can be managed via the admin panel
admin.site.register(Customer)
admin.site.register(Order)
