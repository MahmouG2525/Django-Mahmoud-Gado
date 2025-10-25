from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product') 
    else:
        form = ProductForm()

    return render(request, 'product/add_product.html', {'form': form})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})
