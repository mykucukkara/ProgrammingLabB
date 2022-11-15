from django.http import HttpResponse
from django.shortcuts import render

from product.models import Category, Product, Images, Comment


# Create your views here.

def index(request):
    category = Category.objects.all()
    sliderData = Product.objects.all()[:4]
    dayProducts = Product.objects.all()[:4]
    lastProducts = Product.objects.all().order_by('-id')[:4]
    randomProducts = Product.objects.all().order_by('?')[:4]
    context = {'category': category,
               'sliderData': sliderData,
               'dayProducts': dayProducts,
               'lastProducts': lastProducts,
               'randomProducts': randomProducts
               }
    return render(request, 'index.html', context)

def category_products(request, id, slug):
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'selectedCategory': selectedCategory,
               'products': products,
               'category': category}
    return render(request, 'category_products.html', context)


def product_detail(request,id,slug):
    comment = Comment.objects.filter(product_id = id, status='True')
    category = Category.objects.all()
    products = Product.objects.filter(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'products': products,
               'comments': comment,
               'category': category,
               'images': images}
    return render(request, 'product_detail.html', context)