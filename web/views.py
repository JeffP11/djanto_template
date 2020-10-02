from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("My first web!")

def home(request):
  return render(request, "navbar.html")
