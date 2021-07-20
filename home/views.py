from django.shortcuts import render


def index(request):
    """View to render the home page"""
    return render(request, 'home/index.html')


def error_404(request, exception):
    """View to render a cutom 404 page"""
    return render(request, '../templates/404.html')
