from django.db import models
from product.models import Product

class Order(models.Model):
    customer_name = models.CharField(max_length=100, help_text="Enter your full name")
    email = models.EmailField(help_text="Enter your email address")
    address = models.TextField(help_text="Enter your shipping address")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(help_text="Enter quantity you want to order")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name} - {self.product.name}"
