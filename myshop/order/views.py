from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_order')  
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})

@login_required(login_url='login')
def list_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/list_orders.html', {'orders': orders})

@login_required(login_url='login')
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('list_orders')
