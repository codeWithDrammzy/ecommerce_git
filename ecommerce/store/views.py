from django.shortcuts import render,redirect

def store(request):
    return render(request, 'store/store.html')


def checkout(request):
    return render(request, 'store/checkout.html')

def cart(request):
    return render(request, 'store/cart.html')


# Create your views here.
