from django.views import generic
from django.views.generic import TemplateView
from .forms import ProductForm
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("lista_productos")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# se crea la vista mediante *TemplateView*
class ProductsListView(TemplateView):
    template_name = "products/lista_productos.html"

    def get_context_data(self):
        productos = Product.objects.all()
        print(productos)

        return {"productos": productos}


# se crea la vista mediante generic.ListView
class ProductList2View(generic.ListView):
    model = Product
    template_name = "products/lista_productos_2.html"
    context_object_name = "productos"


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
