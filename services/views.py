"""
all views in here
"""
from django.shortcuts import render
from .models import Category, Photo


def home(request):
    """
    Home page view
    :param request:
    :return:
    """
    photos_low = Photo.objects.order_by('-upload_date')[:4]
    photos_top = Photo.objects.order_by('-upload_date')[4:8]
    context = {
        'photos_low': photos_low,
        'photos_top': photos_top,
    }
    return render(request, 'index.html', context)


def services(request):
    """
    services page view
    :param request:
    :return:
    """
    categories = Category.objects.all()
    category_data = {}

    for category in categories:
        photos = category.photos.all()
        photo_list = [photo.image.url for photo in photos]
        category_data[category.title] = photo_list
    context = {
        "category_data": category_data,
        "categories": categories,
    }
    return render(request, 'services.html', context)


def service(request, pk):
    """
    services page view
    :param request:
    :return:
    """
    category = Category.objects.get(id=pk)
    categories = Category.objects.all()

    photos = category.photos.filter(category_id=pk)
    photo_list = [photo.image.url for photo in photos]
    context = {
        "photo_list": photo_list,
        "category": category,
        "categories": categories,
    }
    return render(request, 'service.html', context)


def prices(request):
    """
    prices view
    :param request:
    :return:
    """
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'prices.html', context)


def contact(request):
    """
    contact view
    :param request:
    :return:
    """
    return render(request, 'contact.html')
