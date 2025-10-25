from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the product name")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Enter the price in USD")
    quantity = models.PositiveIntegerField(help_text="Enter available stock quantity")
    image = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Upload a product image")

    def __str__(self):
        return f"{self.name} (${self.price})"
