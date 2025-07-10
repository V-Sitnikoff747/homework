from django.shortcuts import render, redirect
from . models import Customer, Seller, Product, Sale
from . forms import CustomerForm, SellerForm, ProductForm

def index(request):

    return render(request, 'Sale/main_page.html')


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'Sale/customer_list.html', {'customers': customers})

def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'Sale/add_customer.html', {'form': form})

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'Sale/seller_list.html', {'sellers': sellers})

def add_seller(request):
    form = SellerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('seller_list')
    return render(request, 'Sale/add_seller.html', {'form': form})

def products(request):
    products = Product.objects.all()
    return render(request, 'Sale/products.html', {'products': products})


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'Sale/add_product.html', {'form': form})