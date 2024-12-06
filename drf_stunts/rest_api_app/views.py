from django.http import HttpResponse, HttpRequest
from django.shortcuts import render



def api_index(request: HttpRequest):

    return render(request, 'rest_api_app/api_index.html')

