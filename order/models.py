from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from clients.models import Client

User = get_user_model()
# Create your models here.
class order(models.Model):
    client=models.ForeignKey( 'clients.Client', on_delete=models.CASCADE, )
    operator=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    createOrder = models.DateField(auto_now_add=True)
    Comment= models.CharField(max_length = 500, null=True)
   # deliveryman =models.ForeignKey( 'settings.User', on_delete=models.CASCADE, null=True )
    timeОfdelivery = models.DateField(auto_now_add=True, null=True)
    statusDelivery = models.ForeignKey('order.statusDelivery', on_delete=models.CASCADE)
    totalSum = models.FloatField()
    deliveryAdress = models.ForeignKey('order.deliveryAdress', on_delete=models.CASCADE) 

    def __str__(self):
        return "Заказ от " +  self.createOrder

    class Meta:
        verbose_name_plural ="Заказы"
        verbose_name = "Заказ"

class statusDelivery(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ="Статусы заказов"
        verbose_name = "Статус заказа"
        
class deliveryAdress(models.Model):
    client = models.ForeignKey( 'clients.Client', on_delete=models.CASCADE, )
    adress = models.CharField(max_length = 100)
    typeAdress = models.ForeignKey('order.typeAdressDelivery', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural ="Адреса доставки"
        verbose_name = "Адрес доставки"
    
    def __str__(self):
        return self.adress

class typeAdressDelivery(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
