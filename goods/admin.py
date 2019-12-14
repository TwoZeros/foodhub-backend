from django.contrib import admin

from .models import *

@admin.register(goods, categorygGoods )
class AuthorAdmin(admin.ModelAdmin):
    pass