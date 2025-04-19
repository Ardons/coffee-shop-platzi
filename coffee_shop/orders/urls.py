from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import MyOrderView


urlpatterns = [
    path('mi-orden', MyOrderView.as_view(), name='myorder')
]