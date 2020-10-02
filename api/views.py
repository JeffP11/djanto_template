from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def api(request):
  return HttpResponse("My first API!")

def json_endpoint(request):
    response = {
        'a':1,
        'b':2
    }
    return JsonResponse(response)