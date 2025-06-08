from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'main/home.html')


def products(request):
    product_list = Product.objects.all()
    return render(request, 'main/products.html', {'products': product_list})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'products': products})


def pricing(request):
    return render(request, 'main/pricing.html')


def contact(request):
    return render(request, 'main/contact.html')
