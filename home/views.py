from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import NewUserForm
from home.models import UserProfile
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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category, }
    return render(request, 'login.html', context)




def logout_view(request):
    url = request.META.get('HTTP_REFERER')
    logout(request)
    return HttpResponseRedirect(url)


def signup_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.save()
            return HttpResponseRedirect('/')
    form = NewUserForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form, }
    return render(request, 'signup_view.html', context)