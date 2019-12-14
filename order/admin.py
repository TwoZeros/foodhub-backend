from django.contrib import admin

from .models import *

@admin.register(order, statusDelivery, deliveryAdress )
class AuthorAdmin(admin.ModelAdmin):
    pass