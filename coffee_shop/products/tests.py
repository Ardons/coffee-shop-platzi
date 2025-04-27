from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductList2ViewTests(TestCase):

    def test_should_return_200(self):
        url = reverse("lista_productos_2")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["productos"].count(), 0)

    def test_should_return_200_with_products(self):
        url = reverse("lista_productos_2")
        Product.objects.create(
            name="test",
            description="producto de prueba",
            price="50",
            available=True,
            photo="/hola",
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["productos"].count(), 1)
