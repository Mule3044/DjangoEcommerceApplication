from django.shortcuts import render, get_object_or_404
from product.models import Product
from category.models import Category

# Create your views here.


def product_list(request, category_slug=None):
    categories = None
    products_list = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products_list = Product.objects.filter(
            category=categories, is_available=True)
        product_count = products_list.count()
    else:
        products_list = Product.objects.all().filter(is_available=True)
        product_count = products_list.count()

    context = {
        'products_list': products_list,
        'product_count': product_count,
    }
    return render(request, 'product/product_index.html',  context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request, 'product/product_detail.html', context)
