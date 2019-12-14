from django.urls import path, include
from goods.views import *

app_name = 'goods'
urlpatterns = [
    path('all/', GoodListView.as_view()),
    path('category/all', CategoryListView.as_view()),
]