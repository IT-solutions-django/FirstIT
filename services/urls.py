from django.urls import path, include
from .views import *


app_name = 'services'


urlpatterns = [
    path('', ServicesView.as_view(), name='services'),
]