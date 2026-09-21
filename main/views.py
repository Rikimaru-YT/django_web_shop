from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title
from .forms import ContactMessageForm, ProductCommentForm
from .models import Category, Tag, Brand, Product
from django.db.models import Q

def home_page(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'main/index.html', context)


def shop_page(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(name__icontains=search_query)

    context = {
        'tags': tags,
        'brands': brands,
        'categories': categories,
        'products': products,
        'search_query': search_query,
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


def show_product_detail(request, product_id):
    product_detail = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductCommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product_detail
            form.user = request.user
            form.save()
            return redirect('detail')
    else:
        form = ProductCommentForm()

    context = {
        'product_detail': product_detail,
        'form': form
    }
    return render(request, 'main/detail.html', context)


def search(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query) | Q(full_description__icontains=query)

        )
    else:
        products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'main/search.html', context)

