from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# localhost: 8000/demo

def say_hello(request):
    return HttpResponse("Hello, world!!!!")


def welcome(request, name):
    return render(request, 'index.html', context={'name': ""})
