# products/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product, Category 

def home_page(request):
    context = {
        'page_title': 'Welcome to NextTech.ph',
        'message': 'Your one-stop shop for the latest tech!',
    }
    return render(request, 'products/home.html', context)

def product_list(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all() 

    context = {
        'page_title': 'Our Products',
        'products': all_products,
        'categories': all_categories,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'page_title': product.name, 
        'product': product,          
    }
    return render(request, 'products/product_detail.html', context)
