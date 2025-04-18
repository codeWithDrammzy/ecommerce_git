from django.shortcuts import render,redirect
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
    return render(request, 'store/checkout.html')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete =False)
        items = order.orderitem_set.all()
        oreder_items = OrderItem.objects.count()
    else:
        items=[]

    context ={'items':items,
              'order_items':oreder_items
              }
    return render(request, 'store/cart.html', context)


# Create your views here.
