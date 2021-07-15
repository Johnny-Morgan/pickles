from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review


def all_products(request):
    """ A view to show all products in the store,
    including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search words entered!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'search_word': query,
        'categories': categories,
        'sorting': sorting,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ A view to show individual product information """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id).order_by('-id')

    context = {
        'product': product,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'reviews': reviews,
    }

    return render(request, 'products/product_info.html', context)
