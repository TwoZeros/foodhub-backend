from django.urls import path, include
from clients.views import *

app_name = 'client'
urlpatterns = [
    path('all/', ClientListView.as_view())
]