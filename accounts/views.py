from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': orders.count(),
        'delivered': orders.filter(status='delivered').count(),
        'pending': orders.filter(status='pending').count(),
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    context = {
        'customer': customer,
        'orders': orders,
    }

    return render(request, 'accounts/customer.html', context)


def order_create(request):

    form = OrderForm
    if request.method == 'POST':
        # print('#', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'accounts/order_form.html', context )

def order_update(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'accounts/order_form.html', context )

def order_delete(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')
 
    context = {
        'order': order
    }

    return render(request, 'accounts/order_delete.html', context )
