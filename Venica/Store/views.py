from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.

def Storefront(request):
    return render(request, 'Store/index.html')


def Shop(request):
    return render(request, 'Store/shop.html')


def Product_detail(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
            return render(request, 'Store/productdetail.html', context)
        else:
            messages.error(request, 'Something went wrong')
            return redirect('categories')
        
    else:
        messages.error(request, 'Something went wrong')
        return redirect('categories')

def Wishlist(request):
    return render(request, 'Store/wishlist.html')


def Checkout(request):
    return render(request, 'Store/checkout.html')

def AddCart(request):
    return render(request, 'Store/cart.html')


# categories views


def categories(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'Store/categories.html', context)


def category_view(request, slug):
    if(Category.objects.filter(slug = slug, status=0)):
        products= Product.objects.filter(category__slug = slug)
        category_name = Category.objects.filter(slug = slug).first()
        context = {'products':products, 'category_name': category_name}
        return render(request, 'Store/product_category.html', context)

    else:
        messages.warning(request, 'No such Category')
        return redirect('categories')