from django.urls import path, include
from order.views import *

app_name = 'goods'
urlpatterns = [
    path('all/', OrderListSView.as_view())
]