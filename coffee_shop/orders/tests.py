from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MyOrderViewTests(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse("myorder")
        response = self.client.get(url)
        self.assertEqual(response.url, "/usuarios/login/?next=/ordenes/mi-orden/")

    def test_logged_user_should_redirect(self):
        url = reverse("myorder")
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.url, "/usuarios/login/?next=/ordenes/mi-orden/")
