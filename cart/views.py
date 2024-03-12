from django.shortcuts import render,redirect
from services.models import Services
from .models import Cart, CartItems
from django.http import HttpResponseRedirect
# Create your views here.

def add_to_cart(request, id):
    service = Services.objects.get(id = id)
    user = request.user
    cart= Cart.objects.get_or_create(user = user, is_paid = False)
    cart_item = CartItems.objects.create(cart = cart, service = service)
    cart_item.save()
    return redirect('home')

