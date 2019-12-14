from django.db import models

class goods(models.Model):
    name =models.CharField(max_length = 100, verbose_name="Наименование")
    category = models.ForeignKey('categorygGoods', on_delete=models.CASCADE, verbose_name="Категория товара")
    price = models.FloatField(verbose_name="Цена по прайсу")
    isHealth = models.BooleanField(default=False, verbose_name="Здоровая пища")
    
    def __str__(self):
        return self.name +"/" + self.category.name

    class Meta:
        verbose_name_plural ="Еда"
        verbose_name = "Еда"

class categorygGoods(models.Model):
    name =models.CharField(max_length = 100, null=True)
    isHealth = models.BooleanField(default=False, verbose_name="Здоровая пища")
    isAlhogol = models.BooleanField(default=False, verbose_name="Содердит спирт")

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural ="Категории"
        verbose_name = "Категория"   
# Create your models here.
