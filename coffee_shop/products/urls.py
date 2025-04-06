from django.urls import path
from .views import ProductFormView, ProductsListView


urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name="add_product"),
    path('lista_productos/', ProductsListView.as_view(), name='lista_productos')
]
