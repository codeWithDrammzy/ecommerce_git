from django.shortcuts import render,redirect
from django.http import JsonResponse   
import json 
from .models import  *
import datetime


def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItem = order['get_cart_items']

    product=Product.objects.all()
    oreder_items = OrderItem.objects.count()
   
    
    context ={
        'product':product,
        'order_items':oreder_items,
        'cartItem': cartItem

    }

    return render(request, 'store/store.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItem = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItem': cartItem
    }

    return render(request, 'store/checkout.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False }
        cartItem = order['get_cart_items']
    context = {
        'items': items,
        'cartItem':cartItem,
        'order': order
    }
    return render(request, 'store/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)  # Correct model name
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item updated successfully', safe=False)
# Create your views here.



def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping ==True:
            ShippingAddress.objects.create(
                customer= customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data ['shipping']['state'],
                phone = data['shipping']['phone'],



            )
    else:
        print('User is not logged in')

    return JsonResponse('Payment submitted..', safe=False)

    