from django.shortcuts import render
from django.http import HttpResponse


def sayhello(request):
    return HttpResponse("Hello World!")


def index(request):
    return render(request, 'index.html', {})

