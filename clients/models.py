from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
 
class Client(models.Model):
    fio = models.CharField(max_length=35)
    telephone = models.CharField(max_length = 15,null=True)
    email = models.EmailField(max_length=254, null=True) 
    status_client = models.ForeignKey('Status_client', on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    descriptions = models.CharField(max_length = 500, null=True)

    class Meta:
        verbose_name_plural ="Клиенты"
        verbose_name = "Клиент"
    
    def __str__(self):
        return self.fio
class Status_client(models.Model):
    name = models.CharField(max_length = 35)
    description = models.CharField(max_length = 500,null=True)
    color = models.IntegerField()
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural ="Статусы клиентов"
        verbose_name = "Статус клиента"

class Comment_client(models.Model):
    client=models.ForeignKey( 'Client', on_delete=models.CASCADE, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length = 500)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural ="Коментарии о клиентах"
        verbose_name = "Коментарий о клиенте"



class Task_Manager(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    data_begin = models.DateTimeField(default = timezone.now)
    data_end = models.DateTimeField()
    type_task = (
        ('DO','Выполнено'),
        ('PL','Заполанирована'),
        ('CA','Отменено'),
        ('MO','Перенесено'),
    )
    status_task = models.CharField(max_length = 10, choices =type_task, default ='DO')


    class Meta:
        verbose_name_plural = "Задачи менеджеру"
        verbose_name = "Задача менеджеру"

class History(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    pole = models.CharField(max_length = 100)
    value = models.CharField(max_length = 100)
    data_edit = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = "Истории"
        verbose_name = "История"
    