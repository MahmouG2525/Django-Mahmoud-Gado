from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'name': 'Name of the product.',
            'price': 'Price must be a decimal number (e.g. 29.99).',
            'quantity': 'How many units are available.',
        }
