from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


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

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
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

    # Calculate average rating
    sum_ratings = 0
    if len(reviews) != 0:
        for review in reviews:
            sum_ratings += float(review.rating)
        avg_rating = sum_ratings / len(reviews)
    else:
        avg_rating = None

    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect(reverse('product_info', args=[product.id]))
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'reviews': reviews,
        'review_form': review_form,
        'page_obj': page_obj,
        'rating': avg_rating,
    }

    return render(request, 'products/product_info.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to \
            add a new product.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please \
                ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to \
            edit a product.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} successfully updated!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                           Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to \
            delete a product.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted!')
    return redirect(reverse('products'))


@login_required
def delete_review(request, review_id):
    """ Delete a review from the product page """

    review = get_object_or_404(Review, pk=review_id)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permssion \
            to delete a review.')
        return redirect(reverse('product_info', args=[review.product.id]))

    review.delete()
    messages.success(request, 'Review successfully deleted.')

    return redirect(reverse('product_info', args=[review.product.id]))
