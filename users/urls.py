from django.urls import path, include
from users.views import *

app_name = 'users'
urlpatterns = [
    path('all/', ListUsers.as_view()),
]