from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('products/<slug:slug>', ProductByCategoryView.as_view(), name='products_by_category'),
]