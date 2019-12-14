from django.urls import path, include
from order.views import *

app_name = 'orders'
urlpatterns = [
    path('all/', OrderListSView.as_view())
]