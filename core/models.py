from django.db import models
from django.contrib.auth.models import AbstractUser
from services.models import Services
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default = False)
    is_client = models.BooleanField('Is Client', default=False)
    profile_picture = models.ImageField(upload_to='uploads/', default=1)
    
    
class ServicePurchase(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.service