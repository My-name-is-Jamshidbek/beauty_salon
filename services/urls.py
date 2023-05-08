"""
services all urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('prices/', views.prices, name='prices'),
    path('service/<int:pk>', views.service, name='service'),
    path('contact/', views.contact, name='contact')
]
