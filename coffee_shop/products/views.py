from django.views import generic
from django.views.generic import TemplateView
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Product

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('lista_productos')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#se crea la vista mediante *TemplateView*
class ProductsListView(TemplateView):
    template_name = "products/lista_productos.html"
    
    def get_context_data(self):
        productos = Product.objects.all()
        print(productos)
        
        return {
            "productos": productos
        }

#se crea la vista mediante generic.ListView
class ProductList2View(generic.ListView):
    model = Product
    template_name = "products/lista_productos_2.html"
    context_object_name = 'productos'