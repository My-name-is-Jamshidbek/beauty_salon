from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Home page view
    :param request:
    :return:
    """
    return render(request, 'home.html')
