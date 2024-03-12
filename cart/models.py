from django.db import models
from django.contrib.auth.models import User
from services.models import Services
from django.conf import settings
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    is_paid = models.BooleanField(default=True)
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    service = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, blank = True)
    