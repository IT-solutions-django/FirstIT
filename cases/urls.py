from django.urls import path, include
from .views import *


app_name = 'cases'


urlpatterns = [
    path('', CasesView.as_view(), name='cases'),
]