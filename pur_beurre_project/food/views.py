from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    message = "Ceci est la page des aliments"
    return HttpResponse(message)