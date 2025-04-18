from django.shortcuts import render,redirect
from .models import  *


def store(request):
    product=Product.objects.all()
    context ={
        'product':product
    }

    return render(request, 'store/store.html', context)


def checkout(request):
    return render(request, 'store/checkout.html')

def cart(request):
    return render(request, 'store/cart.html')


# Create your views here.
