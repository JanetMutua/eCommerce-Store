from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.

def Storefront(request):
    return render(request, 'Store/index.html')

# -----------------------------------------------shop view----------------------------------------

def Shop(request):
    products = Product.objects.filter(status=0)
    context = {'products': products}
    return render(request, 'Store/shop.html', context)

# ---------------------------------------------shop selections----------------------------------
def Trending(request):
    products = Product.objects.filter(trending = 1)
    context = {'products': products}
    return render(request, 'Store/trending.html', context)

def Clearance(request):
    products = Product.objects.filter(clearance_sale = 1)
    context = {'products': products}
    return render(request, 'Store/clearance.html', context)


def NewArrival(request):
    products = Product.objects.filter(new_arrival = 1)
    context = {'products': products}
    return render(request, 'Store/newarrival.html', context)


# ----------------------------------------------contact us---------------------------------------
def Contact(request):
    return render(request, 'Store/contact.html')
    
#-------------------------------------------------product views--------------------------------------- 

def Product_detail(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
        else:
            messages.error(request, 'Something went wrong')
            return redirect('categories')
        
    else:
        messages.error(request, 'Something went wrong')
        return redirect('categories')
    return render(request, 'Store/productdetail.html', context)


# ---------------------------------------------------wish list, add to cart, checkout-------------------
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



#---------------------------------------------------size views-----------------------------------------

def Shopsize(request):
    size = Size.objects.filter(status=0)
    context = {'size': size}
    return render(request, 'Store/shopsize.html', context)





# def newarrivals(request, slug):
#     if(Category.objects.filter(slug = slug, new_arrival=1)):
#         products= Product.objects.filter(category__slug = slug)
#         category_name = Category.objects.filter(slug = slug).first()
#         context = {'products':products, 'category_name': category_name}
#         return render(request, 'Store/product_category.html', context)

#     else:
#         messages.warning(request, 'No such Category')
#         return redirect('categories')
