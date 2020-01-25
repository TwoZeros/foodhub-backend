from django.contrib import admin

from .models import *

@admin.register(User )
class AuthorAdmin(admin.ModelAdmin):
    pass