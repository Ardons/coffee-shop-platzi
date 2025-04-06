from django.urls import path
from .views import ProductFormView, ProductsListView, ProductList2View


urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name="add_product"),
    path('lista_productos/', ProductsListView.as_view(), name='lista_productos'),
    path('lista_productos_2/', ProductList2View.as_view(), name='lista_productos_2'),
]
