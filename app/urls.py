from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services')
]
