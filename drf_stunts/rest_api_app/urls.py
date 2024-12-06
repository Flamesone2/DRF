from django.urls import path

from rest_framework.urls import app_name
from .views import api_index


app_name = 'rest_api_app'

urlpatterns = [
    path('', api_index, name= 'api')
]
