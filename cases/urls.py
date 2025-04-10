from django.urls import path, include
from .views import *


app_name = 'cases'


urlpatterns = [
    path('', CasesView.as_view(), name='cases'),
    path('<slug:case_slug>/', CaseView.as_view(), name='case'),
]