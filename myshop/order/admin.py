from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'product', 'quantity', 'created_at')
    search_fields = ('customer_name', 'email')
    list_filter = ('created_at',)
