from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderProductForm

# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order'
    
    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user, is_active=True).first()
    

class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy('myorder')
    
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active = True,
            user=self.request.user
        )
        
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)