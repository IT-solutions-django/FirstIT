from django.urls import path
from .views import *


app_name = 'contacts'


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),

    path('api/save-request/', SaveRequestView.as_view(), name='save_request'),
]