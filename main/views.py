from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import FAQ, Category, Tag, Brand, Product


def home_page(request):
    return render(request, 'main/index.html')


def shop_page(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()

    context = {
        'tags': tags,
        'brands': brands,
        'categories': categories,
        'products': products,
    }
    return render(request, 'main/shop.html', context)


def contacts_page(request):
    if request.method == 'POST':
        form = ContactMessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()

    context = {
        'form': form
    }
    return render(request, 'main/contacts.html', context)

def detail_page(request):
    return render(request, 'main/detail.html')

def cart_page(request):
    return render(request, 'main/cart.html')



"""
на странице shop вывести из базы данных
все категории
все теги
и все бренды
"""