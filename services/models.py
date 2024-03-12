from django.db import models

# Create your models here.
class Services(models.Model):
    service_name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.ImageField( upload_to='uploads/')
    
    def __str__(self):
        return self.service_name
    
    class Meta:
        verbose_name_plural = "Services"
    
class Order(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.service
    