from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('products/by/category/<slug:slug>', ProductByCategoryView.as_view(), name='products_by_category'),
    path('products/detail/<slug:slug>', ProductDetailView.as_view(), name='products_detail'),
]