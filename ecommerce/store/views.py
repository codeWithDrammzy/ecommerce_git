from django.shortcuts import render,redirect
from django.http import JsonResponse    
from .models import  *


def store(request):
    product=Product.objects.all()
    oreder_items = OrderItem.objects.count()
    context ={
        'product':product,
        'order_items':oreder_items
    }

    return render(request, 'store/store.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order
    }

    return render(request, 'store/checkout.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        oreder_items = OrderItem.objects.count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        oreder_items = 0  # Initialize oreder_items to 0 for non-authenticated users

    context = {
        'items': items,
        'order_items': oreder_items,
        'order': order
    }
    return render(request, 'store/cart.html', context)

def updateItem(request):
    
    
    return JsonResponse('Item added sucessfully', safe=False)
# Create your views here.
