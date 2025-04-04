from django.urls import path, include
from .views import *


app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', include('contacts.urls', namespace='contacts')),
]