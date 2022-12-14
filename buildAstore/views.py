from django.shortcuts import render

from .models import Category, Product

# Creating views here.
def all_products(request):
    products = Product.objects.all()[0:6]
    return render(request, 'buildAstore/home.html', {'products': products})

def about(request):
    return render(request, 'buildAstore/about.html')