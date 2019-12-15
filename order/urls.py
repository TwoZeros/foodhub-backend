from django.urls import path, include
from order.views import *

app_name = 'orders'
urlpatterns = [
    path('all/', OrderListSView.as_view()),
    path('detail/<int:pk>/', GoodsByOrderView.as_view())
]