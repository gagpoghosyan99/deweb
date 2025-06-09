from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    return render(request, 'main/home.html')


def product_list(request):
    q = request.GET.get('q', '')  
    products = Product.objects.filter(title__icontains=q).order_by('-created_at')
    return render(request, 'main/products.html', {
        'products': products,
        'query': q,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {
        'product': product
    })


def pricing(request):
    return render(request, 'main/pricing.html')


def contact(request):
    return render(request, 'main/contact.html')
