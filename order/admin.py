from django.contrib import admin

from .models import *

@admin.register(order, goodsByOrder, statusDelivery, deliveryAdress,typeAdressDelivery )
class AuthorAdmin(admin.ModelAdmin):
    pass