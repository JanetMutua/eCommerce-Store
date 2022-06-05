from django.shortcuts import render


# Create your views here.

def Storefront(request):
    return render(request, 'Store/index.html')


def Shop(request):
    return render(request, 'Store/shop.html')


def Product_detail(request):
    return render(request, 'Store/shopdetail.html')

def Wishlist(request):
    return render(request, 'Store/wishlist.html')


def Checkout(request):
    return render(request, 'Store/checkout.html')

def AddCart(request):
    return render(request, 'Store/cart.html')