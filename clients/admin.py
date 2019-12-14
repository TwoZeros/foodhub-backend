from django.contrib import admin
from .models import Client, Comment_client, Status_client, Task_Manager, History

@admin.register(Client, Comment_client, Status_client, Task_Manager, History)
class AuthorAdmin(admin.ModelAdmin):
    pass
# Register your models here.

