from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductByCategoryView(ProductListView):
    template_name = 'shop/shop.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(slug=self.kwargs.get('slug'))
        products = category.products.all()
        # products = Product.objects.filter(category__slug=self.kwargs.get('slug'))
        context['products'] = products
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'product'






