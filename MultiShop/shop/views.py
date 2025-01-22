from django.shortcuts import render
from django.views.generic import ListView

from .models import *

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

