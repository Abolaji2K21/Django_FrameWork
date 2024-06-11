from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# localhost: 8000/demo

def say_hello(request):
    return HttpResponse("Hello World!")


def welcome(request, name):
    return HttpResponse(f"Welcome {name} to my YouTube channel demo!")