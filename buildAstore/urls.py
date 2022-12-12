from django.contrib import admin
from django.urls import path

from . import views

from buildAstore.views import about


app_name = 'buildAstore'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('about/', about, name='about'),
]
