from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def myfirstview(request):
    data = {
        'name': 'Saul'
    }
    return JsonResponse(data)