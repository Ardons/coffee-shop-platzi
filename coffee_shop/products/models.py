from django.utils import timezone
from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    date_create =models.DateTimeField(auto_now_add=True, verbose_name="Field Create")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Field MOD")
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(upload_to="logos/", null=True, blank=True, verbose_name="foto")
    
    def __str__(self):
        return self.name