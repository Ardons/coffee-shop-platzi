from django.urls import path
from .views import ProductFormView, ProductsListView, ProductList2View, ProductListAPI
from django.http import HttpResponse

urlpatterns = [
    path("produc/", ProductList2View.as_view(), name="lista_productos_2"),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
    path("lista_productos/", ProductsListView.as_view(), name="lista_productos"),    
    path("api/", ProductListAPI.as_view(), name="api"),
]

#lista_productos_2/
#lambda request: HttpResponse("OK - Fast Test!") path("", ProductList2View.as_view(), name="lista_productos_2")