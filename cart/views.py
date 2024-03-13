from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from services.models import Services
from .models import Cart, CartItems
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


def add_to_cart(request, id):
    service = Services.objects.get(id = id)
    user = request.user
    
    if not user.is_authenticated:
        messages.warning(request, "You need to log in to add items to your cart.")
        return redirect(reverse('userLogin'))
    
    cart, _ = Cart.objects.get_or_create(user = user, is_paid = False)
    cart_item = CartItems.objects.create(cart = cart, service = service)
    cart_item.save()
    messages.success(request, "Item added to cart successfully.")
    return redirect('show_cart')

def show_cart(request):
    user = request.user
    cart_items = CartItems.objects.filter(cart__user=user, cart__is_paid=False)
    return render(request, 'show_cart.html', {'cart_items': cart_items})

