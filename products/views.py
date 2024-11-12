from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

# Create your views here.

#cbv
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()
    template_name = "products/list.html"

    #def get_context_data(self, *args, **kwargs):
        #context = super(ProductListView, self).get_context_data(*args, **kwargs)
        #print(context)
        #return context

#fbv
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)   