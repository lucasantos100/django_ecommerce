from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

# Create your views here.
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()